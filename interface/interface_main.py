import sys
import os
from enum import Enum

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QTextBrowser,
    QComboBox,
    QFrame,
    QTabWidget,
    QLineEdit,
    QPushButton,
    QGroupBox,
    QMessageBox,
    QVBoxLayout,
    QStackedWidget,
    QScrollArea,
    QHBoxLayout,
)
from PySide6.QtCore import (
    QFile,
    Qt,
    QMimeData,
    QCoreApplication,
    QUrl,
    QPropertyAnimation,
    QRect,
    QDate,
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QDrag, QPixmap, QPainter, QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView

from cold_storage import db as cs_db
from recipe import db as recipe_db
from setting import db as setting_db

from interface.interface_interaction import InterfaceInteraction, TabKind, RecipeTabKind
from interface.ref_card import RefCard
from interface.recipe_btn_box import RecipeBtnBox
from interface.recommand_feed_box import RecommandFeedBox


class OrderingType(Enum):
    LATEST = "등록 최신순"
    OLDEST = "등록 오래된순"
    EXPIRING_SOON = "소비기한 임박순"


class FoodType(Enum):
    FRUIT_VEGETABLE = "과일 & 채소"
    MEAT = "육류"
    SEA_FOOD = "어류"
    OTHER = "기타"


class RefModalType(Enum):
    ADD = "add"
    EDIT = "edit"

font_sizes = [9, 10, 12, 14]

class Mainwindow:
    # UIs
    window = None
    add_ref_modal = None
    search_manage_ref_modal = None
    recipe_info_modal = None

    # Status
    is_show_only_favorite = False

    ref_modal_type = RefModalType.ADD
    now_edit_ref_id = None

    ref_tab_meat_ordering = OrderingType.LATEST
    ref_tab_sea_food_ordering = OrderingType.LATEST
    ref_tab_fruit_vegetable_ordering = OrderingType.LATEST
    ref_tab_other_ordering = OrderingType.LATEST

    now_display_recipe = None

    gemini_api_key = None
    font_size = None

    # Datas
    all_ref_cards = []

    def load_ui(self, file_name):
        ui_file = QFile(os.path.join(os.path.dirname(__file__), f"{file_name}.ui"))
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        ui = loader.load(ui_file)
        ui_file.close()
        return ui

    def setup_ui(self):
        self.window = self.load_ui("material_stat")
        self.add_ref_modal = self.load_ui("add_ref_modal")
        self.search_manage_ref_modal = self.load_ui("search_manage_ref_modal")

        self.recipe_info_modal = self.load_ui("recipe_info_modal")
        self.recipe_info_modal.serving_1_btn.clicked.connect(
            lambda: self.change_servings_with_gemini(1)
        )
        self.recipe_info_modal.serving_2_btn.clicked.connect(
            lambda: self.change_servings_with_gemini(2)
        )
        self.recipe_info_modal.serving_3_btn.clicked.connect(
            lambda: self.change_servings_with_gemini(3)
        )
        self.recipe_info_modal.serving_4_btn.clicked.connect(
            lambda: self.change_servings_with_gemini(4)
        )
        self.recipe_info_modal.serving_5_btn.clicked.connect(
            lambda: self.change_servings_with_gemini(5)
        )

        self.window.setting_save_btn.clicked.connect(self.save_settings)

        for i in range(1, 5):
            frame = self.window.findChild(QFrame, f"search_frame_{i}")
            if frame:
                frame.setVisible(False)

        self.window.recipe_search_box.textChanged.connect(
            self.toggle_button_by_lineedit
        )
        self.toggle_button_by_lineedit()

        self.place_recommand_feed_boxes()

        # font_sizes 
        self.window.font_size_cbx.addItems([str(size) for size in font_sizes])

    def display_none_all_tabs(self):
        tab_cnt = self.window.tab_root.count()
        for i in range(0, tab_cnt):
            self.window.tab_root.setTabVisible(i, False)

    def display_none_tab_recipe(self):
        tab = self.window.findChild(QTabWidget, "tab_root")
        tab_2 = tab.findChild(QTabWidget, "recip_search_box_tab")
        tab_2.tabBar().hide()

    def setup_combo_box(self):
        combo = self.add_ref_modal.findChild(QComboBox, "type_combo_box")
        if combo:
            combo.clear()
            lists = [i.value for i in FoodType]
            combo.addItems(lists)
        else:
            print("type_combo_box를 찾을 수 없습니다.")

    def show(self):
        app = QApplication(sys.argv)

        self.setup_ui()
        self.window.setWindowTitle("냉장고를 부탁해")
        self.add_ref_modal.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.search_manage_ref_modal.setWindowTitle("재료 보관방법 검색창")

        InterfaceInteraction.setting_events(self)

        self.display_none_all_tabs()
        self.display_none_tab_recipe()
        self.window.tab_root.setCurrentIndex(TabKind.STORAGE_STATUS.value)

        self.setup_combo_box()
        self.setup_sort_btn()

        self.clear_ref_modal()

        self.ref_get_all()

        self.draw_all_ref_cards()

        self.add_recipe_btns_by_type(FoodType.MEAT, "recipe_btn_scrollArea")
        self.add_recipe_btns_by_type(FoodType.SEA_FOOD, "fish_btn_scrollArea")
        self.add_recipe_btns_by_type(
            FoodType.FRUIT_VEGETABLE, "vegetable_btn_scrollArea"
        )
        self.add_recipe_btns_by_type(FoodType.OTHER, "other_btn_scrollArea")

        icon_file_path = os.path.join(os.path.dirname(__file__), "main_icon.jpg")
        main_icon = QIcon(icon_file_path)

        self.window.setWindowIcon(main_icon)
        self.search_manage_ref_modal.setWindowIcon(main_icon)
        self.recipe_info_modal.setWindowIcon(main_icon)

        if self.load_settings():
            app_font = app.font()
            app_font.setPointSize(int(self.font_size.value))
            app.setFont(app_font)

        self.window.show()

        sys.exit(app.exec())

    def show_add_ref_modal(self):
        self.ref_modal_type = RefModalType.ADD
        self.show_ref_modal()

    def show_edit_ref_modal(self, ref_data: cs_db.Ref):
        self.ref_modal_type = RefModalType.EDIT
        self.now_edit_ref_id = ref_data.id

        self.add_ref_modal.name_line_edit.setText(ref_data.Food_name)
        self.add_ref_modal.amount_line_edit.setText(str(ref_data.Amount))
        self.add_ref_modal.expiration_duration_date_edit.setDate(
            QDate.fromString(ref_data.Expiration_date, "yyyy-MM-dd")
        )
        index = self.add_ref_modal.type_combo_box.findText(ref_data.Food_type)

        if index != -1:
            self.add_ref_modal.type_combo_box.setCurrentIndex(index)

        self.show_ref_modal()

    def show_ref_modal(self):
        button_bottom = self.window.ref_add_self_btn.mapToGlobal(
            self.window.ref_add_self_btn.rect().bottomLeft()
        )
        combo_x = button_bottom.x()
        combo_y = button_bottom.y() + ((self.window.height() / 3) - 30)
        self.add_ref_modal.setGeometry(combo_x, combo_y, self.add_ref_modal.width(), 25)

        self.add_ref_modal.show()

    def ok_ref_modal(self):
        if self.ref_modal_type == RefModalType.ADD:
            self.create_ref()
        elif self.ref_modal_type == RefModalType.EDIT:
            self.edit_ref()

    def edit_ref(self):
        food_name = self.add_ref_modal.name_line_edit.text()
        amount = self.add_ref_modal.amount_line_edit.text()
        expiration_date = self.add_ref_modal.expiration_duration_date_edit.text()
        food_type = self.add_ref_modal.type_combo_box.currentText()

        print(f"Editing ref: {food_name}, {amount}, {expiration_date}, {food_type}")

        if cs_db.Database.update(
            self.now_edit_ref_id, food_name, amount, expiration_date, food_type
        ):
            print("Ref updated successfully.")

            for i in self.all_ref_cards:
                if i.ref_data.id == self.now_edit_ref_id:
                    print(f"Updating ref card with id: {self.now_edit_ref_id}")
                    i.ref_data.Food_name = food_name
                    i.ref_data.Amount = amount
                    i.ref_data.Expiration_date = expiration_date
                    i.ref_data.Food_type = food_type
                    break

            self.close_ref_modal()

            self.draw_ref_cards(food_type=FoodType(food_type))

        else:
            print("Failed to update ref.")

    def show_search_manage_ref_modal(self):
        # button_bottom = self.window..mapToGlobal(self.window.ref_add_self_btn.rect().bottomLeft())
        # combo_x = button_bottom.x()
        # combo_y = button_bottom.y() + ((self.window.height() / 3) - 30)
        # self.add_ref_modal.setGeometry(combo_x, combo_y, self.add_ref_modal.width(), 25)

        self.search_manage_ref_modal.show()

    def search_ref_manage(self):
        search_text = self.search_manage_ref_modal.name_edit.text() + " 보관 방법"

        self.search_manage_ref_modal.youtube_view.load(
            QUrl(f"https://www.youtube.com/results?search_query={search_text}")
        )
        self.search_manage_ref_modal.google_view.load(
            QUrl(f"https://www.google.com/search?q={search_text}")
        )

    def change_tab(self, tab_widget, tab_kind):
        tab_widget.setCurrentIndex(tab_kind.value)
        print(f"Changed tab to {tab_kind.value} ({tab_kind.name})")

    def change_tab_recipe(self, tab_kind):
        tab = self.window.findChild(QTabWidget, "tab_root")
        tab_2 = tab.findChild(QTabWidget, "recip_search_box_tab")
        tab_2.setCurrentIndex(tab_kind.value)

    def create_ref(self):
        food_name = self.add_ref_modal.name_line_edit.text()
        amount = self.add_ref_modal.amount_line_edit.text()
        expiration_date = self.add_ref_modal.expiration_duration_date_edit.text()
        food_type = self.add_ref_modal.type_combo_box.currentText()
        print(f"Creating ref: {food_name}, {amount}, {expiration_date}, {food_type}")

        lastrow_id = cs_db.Database.data_insert(
            food_name, amount, expiration_date, food_type
        )

        new_ref = cs_db.Ref(
            id=lastrow_id,
            Food_name=food_name,
            Amount=amount,
            Expiration_date=expiration_date,
            Food_type=food_type,
        )

        ref_card = RefCard(
            new_ref,
            delete_callback=self.delete_ref,
            edit_callback=self.show_edit_ref_modal,
            favorite_callback=self.change_ref_card_favorite,
        )
        self.all_ref_cards.append(ref_card)
        self.draw_ref_cards(food_type=FoodType(food_type))

        self.close_ref_modal()

        if food_type == FoodType.MEAT.value:
            self.add_recipe_btns_by_type(FoodType.MEAT, "recipe_btn_scrollArea")

        if food_type == FoodType.SEA_FOOD.value:
            self.add_recipe_btns_by_type(FoodType.SEA_FOOD, "fish_btn_scrollArea")

        if food_type == FoodType.FRUIT_VEGETABLE.value:
            self.add_recipe_btns_by_type(
                FoodType.FRUIT_VEGETABLE, "vegetable_btn_scrollArea"
            )

        if food_type == FoodType.OTHER.value:
            self.add_recipe_btns_by_type(FoodType.OTHER, "other_btn_scrollArea")

    def draw_all_ref_cards(self):
        self.draw_ref_cards(FoodType.MEAT)
        self.draw_ref_cards(FoodType.SEA_FOOD)
        self.draw_ref_cards(FoodType.FRUIT_VEGETABLE)
        self.draw_ref_cards(FoodType.OTHER)

    def draw_ref_cards(self, food_type: FoodType):
        print(f"draw ref cards Food type : {food_type.value}, ")

        ref_cards = self.get_ref_cards_by_food_type(food_type)

        if not ref_cards:
            print(f"{food_type.value}에 해당하는 재료가 없습니다.")
            return

        if self.is_show_only_favorite:
            ref_cards = [i for i in ref_cards if i.ref_data.is_favorite == True]

        scroll_area_content = None
        ordering = None
        match food_type:
            case FoodType.MEAT:
                scroll_area_content = self.window.meat_scroll_area_content
                ordering = self.ref_tab_meat_ordering
            case FoodType.SEA_FOOD:
                scroll_area_content = self.window.sea_food_scroll_area_content
                ordering = self.ref_tab_sea_food_ordering
            case FoodType.FRUIT_VEGETABLE:
                scroll_area_content = self.window.fruit_vegetable_scroll_area_content
                ordering = self.ref_tab_fruit_vegetable_ordering
            case FoodType.OTHER:
                scroll_area_content = self.window.other_scroll_area_content
                ordering = self.ref_tab_other_ordering

        if not scroll_area_content:
            print(f"{food_type.value} 스크롤 영역을 찾을 수 없습니다.")
            return

        match ordering:
            case OrderingType.LATEST:
                ref_cards = sorted(ref_cards, key=lambda x: x.ref_data.created_at)
            case OrderingType.OLDEST:
                ref_cards = sorted(
                    ref_cards, key=lambda x: x.ref_data.created_at, reverse=True
                )
            case OrderingType.EXPIRING_SOON:
                ref_cards = sorted(
                    ref_cards, key=lambda x: x.ref_data.Expiration_date, reverse=True
                )
            case _:
                print("Unknown ordering type, using default (latest)")

        layout = scroll_area_content.layout()

        # remove origin ref cards
        for i in scroll_area_content.findChildren(RefCard):
            layout.removeWidget(i)
            i.setParent(None)

        # inser new ref cards
        for i in ref_cards:
            layout.insertWidget(2, i)

    def get_ref_cards_by_food_type(self, food_type: FoodType):
        ref_cards = []
        for i in self.all_ref_cards:
            if i.ref_data.Food_type == food_type.value:
                card = RefCard(
                    i.ref_data,
                    delete_callback=self.delete_ref,
                    edit_callback=self.show_edit_ref_modal,
                    favorite_callback=self.change_ref_card_favorite,
                )

                ref_cards.append(card)

        return ref_cards

    def setup_sort_btn(self):
        from .sort_combo_box import setup_ui

        setup_ui(
            self.window.meat_sort_btn,
            FoodType.MEAT,
            callback_func=self.get_ordering_type,
        )
        setup_ui(
            self.window.sea_food_sort_btn,
            FoodType.SEA_FOOD,
            callback_func=self.get_ordering_type,
        )
        setup_ui(
            self.window.fruit_vegetable_sort_btn,
            FoodType.FRUIT_VEGETABLE,
            callback_func=self.get_ordering_type,
        )
        setup_ui(
            self.window.other_sort_btn,
            FoodType.OTHER,
            callback_func=self.get_ordering_type,
        )

    def animation_search_box(self, search_box_name):
        search_box = self.window.findChild(QFrame, f"{search_box_name}")

        if not search_box:
            print(f"{search_box_name}를 찾을 수 없습니다.")
            return

        if search_box.isVisible() and search_box.maximumHeight() > 0:
            start_hight = search_box.height()
            end_hight = 0
            self.anim = QPropertyAnimation(search_box, b"maximumHeight")
            self.anim.setDuration(300)
            self.anim.setStartValue(start_hight)
            self.anim.setEndValue(end_hight)
            self.anim.start()
        else:
            search_box.setVisible(True)
            start_hight = search_box.maximumHeight()
            end_hight = search_box.height() + 100
            self.anim = QPropertyAnimation(search_box, b"maximumHeight")
            self.anim.setDuration(300)
            self.anim.setStartValue(start_hight)
            self.anim.setEndValue(end_hight)
            self.anim.start()

    def popup_animation_from_point(self, widget, start_x, start_y):
        widget = self.window.findChild(QFrame, f"{widget}")

        if not widget:
            print("위젯이 없습니다.")
            return

        widget.setVisible(True)
        widget.repaint()
        QCoreApplication.processEvents()
        end_rect = widget.geometry()
        start_rect = QRect(start_x, start_y, 27, 1)

        widget.setGeometry(start_rect)

        anim = QPropertyAnimation(widget, b"geometry")
        anim.setDuration(300)
        anim.setStartValue(start_rect)
        anim.setEndValue(end_rect)
        anim.start()
        widget._popup_anim = anim

        def fix_geometry():
            widget.setGeometry(end_rect)

        anim.finished.connect(fix_geometry)

    def toggle_button_by_lineedit(self):
        lineedit = self.window.findChild(QLineEdit, "recipe_search_box")
        button = self.window.findChild(QPushButton, "X_recipe_btn")
        if lineedit and button:
            if lineedit.text().strip():
                button.setVisible(True)
            else:
                button.setVisible(False)

    def clear_line_edit(self):
        lineedit = self.window.findChild(QLineEdit, "recipe_search_box")
        if lineedit:
            lineedit.clear()
            self.toggle_button_by_lineedit()

    def add_recipe_btns_by_type(self, food_type: FoodType, scroll_area_name: str):
        from cold_storage import db as cs_db

        names = [
            ref.Food_name
            for ref in cs_db.Database.get_all()
            if ref.Food_type == food_type.value
        ]

        find_scroll_area = self.window.findChild(QTabWidget, "recip_search_box_tab")
        scroll_area = find_scroll_area.findChild(QScrollArea, scroll_area_name)
        if not scroll_area:
            print(f"{scroll_area_name} 스크롤 영역을 찾을 수 없습니다.")
            return

        feed_box_layout = scroll_area.widget()
        if not feed_box_layout:
            print(f"{scroll_area_name}의 컨텐츠 위젯을 찾을 수 없습니다.")
            return

        grid_layout = feed_box_layout.layout()
        if not isinstance(grid_layout, QGridLayout):
            print(f"{scroll_area_name}의 QGridLayout을 찾을 수 없습니다.")
            return

        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0, 0, 5, 0)

        while grid_layout.count():
            item = grid_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()

        max_per_row = 6
        for idx, name in enumerate(names):
            btn_box = RecipeBtnBox(name)
            row = idx % 2
            col = idx // 2
            grid_layout.addWidget(btn_box, row, col)

        if len(names) > max_per_row:
            min_btn_width = 120
            max_col = (len(names) + 1) // 2
            min_width = max(max_col, max_per_row) * min_btn_width
            feed_box_layout.setMinimumWidth(min_width)

    def ref_get_all(self):
        from interface.ref_card import RefCard

        refs = cs_db.Database.get_all()

        ref_cards = []
        for i in refs:
            card = RefCard(
                i,
                delete_callback=self.delete_ref,
                edit_callback=self.show_edit_ref_modal,
                favorite_callback=self.change_ref_card_favorite,
            )
            ref_cards.append(card)

        self.all_ref_cards = ref_cards

    def show_only_favorite(self):
        if self.is_show_only_favorite:
            self.is_show_only_favorite = False
            self.window.fav_ch_btn.setText("즐겨찾는 재료")
        else:
            self.is_show_only_favorite = True
            self.window.fav_ch_btn.setText("X")

        self.draw_all_ref_cards()

    def close_ref_modal(self):
        self.clear_ref_modal()
        self.add_ref_modal.close()

    def clear_ref_modal(self):
        self.now_edit_ref_id = None
        self.add_ref_modal.name_line_edit.clear()
        self.add_ref_modal.amount_line_edit.clear()
        self.add_ref_modal.expiration_duration_date_edit.setDate(QDate.currentDate())
        self.add_ref_modal.type_combo_box.setCurrentIndex(0)

    def get_ordering_type(self, food_type: FoodType, ordering: str):
        print(f"Ordering type: {ordering} for {food_type.value}")

        ordering_type = None
        match ordering:
            case OrderingType.LATEST.value:
                ordering_type = OrderingType.LATEST
            case OrderingType.OLDEST.value:
                ordering_type = OrderingType.OLDEST
            case OrderingType.EXPIRING_SOON.value:
                ordering_type = OrderingType.EXPIRING_SOON
            case _:
                print("Unknown ordering type, using default (latest)")
                ordering_type = OrderingType.LATEST

        match food_type:
            case FoodType.MEAT:
                self.ref_tab_meat_ordering = ordering_type
            case FoodType.SEA_FOOD:
                self.ref_tab_sea_food_ordering = ordering_type
            case FoodType.FRUIT_VEGETABLE:
                self.ref_tab_fruit_vegetable_ordering = ordering_type
            case FoodType.OTHER:
                self.ref_tab_other_ordering = ordering_type

        self.draw_ref_cards(food_type=food_type)

    def delete_ref(self, ref_id: int):
        result = QMessageBox.question(
            None, "재료 삭제", "정말로 이 재료를 삭제하시겠습니까?"
        )
        if result == QMessageBox.StandardButton.Yes:
            if cs_db.Database.delete(ref_id):
                self.all_ref_cards = [
                    i for i in self.all_ref_cards if i.ref_data.id != ref_id
                ]
                self.draw_all_ref_cards()
                print(f"Deleted ref with id: {ref_id}")

                # ★ 육류 재료가 삭제되었을 때 버튼 갱신
                self.add_recipe_btns_by_type(FoodType.MEAT, "recipe_btn_scrollArea")
                self.add_recipe_btns_by_type(FoodType.SEA_FOOD, "fish_btn_scrollArea")
                self.add_recipe_btns_by_type(
                    FoodType.FRUIT_VEGETABLE, "vegetable_btn_scrollArea"
                )
                self.add_recipe_btns_by_type(FoodType.OTHER, "other_btn_scrollArea")
            else:
                print(f"Failed to delete ref with id: {ref_id}")

    def change_ref_card_favorite(self, ref_id: int, food_type: str, is_favorite: bool):
        for card in self.all_ref_cards:
            if card.ref_data.id == ref_id:
                card.set_favorite(is_favorite)
                break

        self.draw_ref_cards(food_type=FoodType(food_type))

    def search_ref_by_name(self, food_type: FoodType):
        name = ""

        match food_type:
            case FoodType.MEAT:
                name = self.window.ref_search_box_1.text()
            case FoodType.SEA_FOOD:
                name = self.window.ref_search_box_4.text()
            case FoodType.FRUIT_VEGETABLE:
                name = self.window.ref_search_box_2.text()
            case FoodType.OTHER:
                name = self.window.ref_search_box_3.text()

        print(f"Searching for '{name}' in {food_type.value}")

        if not name:
            print("검색어가 비어 있습니다. 값을 전체로 검색합니다.")
            self.ref_get_all()
            self.draw_ref_cards(food_type=food_type)
            return

        self.ref_get_all()
        refs = self.all_ref_cards

        filtered_refs = [
            ref
            for ref in refs
            if name.lower() in ref.ref_data.Food_name.lower()
            and ref.ref_data.Food_type == food_type.value
        ]

        if not filtered_refs:
            print(f"{food_type.value}에 해당하는 '{name}' 재료가 없습니다.")
            QMessageBox.information(
                None,
                "검색 결과",
                f"{food_type.value}에 해당하는 '{name}' 재료가 없습니다.",
            )
            return

        ref_cards = []
        for i in filtered_refs:
            card = RefCard(
                i.ref_data,
                delete_callback=self.delete_ref,
                edit_callback=self.show_edit_ref_modal,
                favorite_callback=self.change_ref_card_favorite,
            )
            ref_cards.append(card)

        self.all_ref_cards = ref_cards
        self.draw_ref_cards(food_type=food_type)

    def place_recommand_feed_boxes(self):
        # recommand_feed_scrollarea(QScrollArea)에서 내부 위젯과 QGridLayout 찾기
        scroll_area = self.window.findChild(QScrollArea, "recommand_feed_scrollarea")
        if not scroll_area:
            print("recommand_feed_scrollarea(QScrollArea)를 찾을 수 없습니다.")
            return

        content_widget = scroll_area.widget()
        if not content_widget:
            print("recommand_feed_scrollarea의 컨텐츠 위젯을 찾을 수 없습니다.")
            return

        grid_layout = content_widget.layout()
        if not isinstance(grid_layout, QGridLayout):
            print("recommand_feed_scrollarea의 QGridLayout을 찾을 수 없습니다.")
            return

        # 기존 위젯 모두 제거
        while grid_layout.count():
            item = grid_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()


        # 예시로 10개의 추천 박스 생성, 가로 3개씩 배치
        recipe_ids = [
            7052101,
            7022775,
            7033948,
            7029097,
            7035751,
            7052101,
            7022775,
            7035751,
            7018465,
            7052101,
            7022775,
            7035751,
            6984517,
            7025833,
            7009944,
            6993517,
            7003487,
            7005830,
        ]

        for idx in recipe_ids:
            feed_box = RecommandFeedBox(
                recipe_id=idx,
                title_label=f"Title {idx+1}",
                tag_label=f"#Tag {idx+1}",
                img="D:/대학/team-project/interface/test_cat.jpg",
                parent=content_widget,
                open_modal_callback=self.open_recipe_info_modal,
            )
            row = idx // 3  # 3개씩 한 행
            col = idx % 3
            grid_layout.addWidget(feed_box, row, col)

    def open_recipe_info_modal(self, recipe_id: int):
        recipe_data = recipe_db.Database.get_with_id(recipe_id)
        if not recipe_data:
            print(f"레시피 ID {recipe_id}를 찾을 수 없습니다.")
            return

        self.now_display_recipe = recipe_data
        self.recipe_info_modal.setWindowTitle(recipe_data.title)

        self.recipe_info_modal.youtube_w_view.load(
            QUrl(
                f"https://www.youtube.com/@%EB%A7%8C%EA%B0%9C%EC%9D%98%EB%A0%88%EC%8B%9C%ED%94%BC/search?query={recipe_data.title}"
            )
        )

        level = ""
        match recipe_data.level:
            case "초급":
                level = "⭐⭐⭐"
            case "아무나":
                level = "⭐⭐"
            case "중급":
                level = "⭐⭐⭐⭐"
            case "고급":
                level = "⭐⭐⭐⭐⭐"
            case "":
                level = "⭐"

        self.recipe_info_modal.name_level_lbl.setText(f"{recipe_data.title} {level}")

        self.recipe_info_modal.cooking_time_lbl.setText(recipe_data.cooking_time)
        self.recipe_info_modal.origin_servings_lbl.setText(recipe_data.servings)

        ingredients = recipe_data.ingredients.replace(" | ", "\n").replace("] ", "]\n")
        self.recipe_info_modal.ingredient_lbl.setText(ingredients)

        steps = recipe_data.steps.replace(" | ", "\n\n")
        self.recipe_info_modal.step_txt_browser.setText(steps)
        return True

        self.recipe_info_modal.show()

    def change_servings_with_gemini(self, servings: int):
        if not self.now_display_recipe:
            print("현재 표시된 레시피가 없습니다.")
            return

        if not self.gemini_api_key:
            QMessageBox.warning(
                self.recipe_info_modal,
                "경고",
                "설정페이지에서 Gemini API 키를 설정해주세요.",
            )
            return

    def load_settings(self):
        self.gemini_api_key = setting_db.Database.get_gemini_api_key()
        print(f"Loaded Gemini API Key: {self.gemini_api_key}")
        self.window.gemini_api_keyLineEdit.setText(self.gemini_api_key.value or "")

        self.font_size = setting_db.Database.get_font_size()
        if self.font_size is None:
            print("Font size setting not found, using default value.")
            return False
        else:
            print(f"Loaded font size: {self.font_size.value}")
            self.window.font_size_cbx.setCurrentText(self.font_size.value)
            return True

    def save_settings(self):
        gemini_api_key = self.window.gemini_api_keyLineEdit.text()
        if not gemini_api_key.strip():
            QMessageBox.warning(
                self.window,
                "경고",
                "Gemini API 키를 입력해주세요.",
            )
            return

        print(f"Saving settings: Gemini API Key = {gemini_api_key}")

        if self.gemini_api_key is None:
            setting_db.Database.create("gemini_api_key", gemini_api_key)
        else:
            setting = setting_db.Database.get_with_name("gemini_api_key")
            if setting is not None:
                setting.value = gemini_api_key
                setting_db.Database.update(setting)

        now_font_size = self.window.font_size_cbx.currentText()
        print(f"Saving settings: Font size = {now_font_size}")
        if self.font_size is None:
            setting_db.Database.create("font_size", str(now_font_size))
            print("Font size setting created.")
        else:
            setting = setting_db.Database.get_with_name("font_size")
            if setting is not None:
                setting.value = str(now_font_size)
                setting_db.Database.update(setting)

            print("Font size setting updated.")
        
        QMessageBox.information(
            self.window,
            "설정 저장",
            "설정이 저장되었습니다. 프로그램을 재시작해주세요.",
        )
