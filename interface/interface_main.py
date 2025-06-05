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
)
from PySide6.QtCore import (
    QFile, 
    Qt, 
    QMimeData, 
    QCoreApplication, 
    QUrl,
    QPropertyAnimation,
    QRect,
    QDate
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QDrag, QPixmap, QPainter
from PySide6.QtWebEngineWidgets import QWebEngineView

from cold_storage import db as cs_db
from interface.interface_interaction import InterfaceInteraction, TabKind, RecipeTabKind
from interface.ref_card import RefCard

class FoodType(Enum):
    FRUIT_VEGETABLE = "과일 & 채소"
    MEAT = "육류"
    SEA_FOOD = "어류"
    OTHER = "기타"

class Mainwindow:
    # UIs
    window = None
    add_ref_modal = None
    search_manage_ref_modal = None

    # Status
    is_show_only_favorite = False

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
        for i in range(1, 5):
            frame = self.window.findChild(QFrame, f"search_frame_{i}")
            if frame:
                frame.setVisible(False)
        self.window.recipe_search_box.textChanged.connect(self.toggle_button_by_lineedit)
        self.toggle_button_by_lineedit()


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
        self.add_ref_modal.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.search_manage_ref_modal.setWindowTitle('재료 보관방법 검색창')

        InterfaceInteraction.setting_events(self)

        self.display_none_all_tabs()
        self.display_none_tab_recipe()
        self.window.tab_root.setCurrentIndex(TabKind.STORAGE_STATUS.value)

        self.setup_combo_box()
        self.setup_sort_btn()

        self.close_add_ref_modal()

        self.all_ref_card = self.get_all_ref_cards()

        self.draw_all_ref_cards()

        self.window.show()

        sys.exit(app.exec())

    def show_add_ref_modal(self):
        button_bottom = self.window.ref_add_self_btn.mapToGlobal(
            self.window.ref_add_self_btn.rect().bottomLeft()
        )
        combo_x = button_bottom.x()
        combo_y = button_bottom.y() + ((self.window.height() / 3) - 30)
        self.add_ref_modal.setGeometry(combo_x, combo_y, self.add_ref_modal.width(), 25)

        self.add_ref_modal.show()

    def show_search_manage_ref_modal(self):
        # button_bottom = self.window..mapToGlobal(self.window.ref_add_self_btn.rect().bottomLeft())
        # combo_x = button_bottom.x()
        # combo_y = button_bottom.y() + ((self.window.height() / 3) - 30)
        # self.add_ref_modal.setGeometry(combo_x, combo_y, self.add_ref_modal.width(), 25)

        self.search_manage_ref_modal.show()

    def search_ref_manage(self):
        search_text = self.search_manage_ref_modal.name_edit.text() + " 보관 방법"

        self.search_manage_ref_modal.youtube_view.load(QUrl(f"https://www.youtube.com/results?search_query={search_text}"))
        self.search_manage_ref_modal.google_view.load(QUrl(f"https://www.google.com/search?q={search_text}"))



    def change_tab(self, tab_widget, tab_kind):
        tab_widget.setCurrentIndex(tab_kind.value)
        print(f"Changed tab to {tab_kind.value} ({tab_kind.name})")

    def change_tab_recipe(self, tab_kind):
        tab = self.window.findChild(QTabWidget, "tab_root")
        tab_2 = tab.findChild(QTabWidget, "recip_search_box_tab")
        tab_2.setCurrentIndex(tab_kind.value)


    # TODO: add validation, insert error handling
    def create_ref(self):
        food_name = self.add_ref_modal.name_line_edit.text()
        amount = self.add_ref_modal.amount_line_edit.text()
        expiration_date = self.add_ref_modal.expiration_duration_date_edit.text()
        food_type = self.add_ref_modal.type_combo_box.currentText()
        print(f"Creating ref: {food_name}, {amount}, {expiration_date}, {food_type}")

        lastrow_id = cs_db.Database.data_insert(food_name, amount, expiration_date, food_type)

        new_ref = cs_db.Ref(id=lastrow_id, Food_name=food_name, Amount=amount, Expiration_date=expiration_date, Food_type=food_type)

        ref_card = RefCard(new_ref)
        self.all_ref_cards.append(ref_card)
        self.draw_ref_cards(food_type=FoodType(food_type))

        self.close_add_ref_modal(only_clear=True)

    def draw_all_ref_cards(self, is_only_favorite=False):
        self.draw_ref_cards(FoodType.MEAT, is_only_favorite)
        self.draw_ref_cards(FoodType.SEA_FOOD, is_only_favorite)
        self.draw_ref_cards(FoodType.FRUIT_VEGETABLE, is_only_favorite)
        self.draw_ref_cards(FoodType.OTHER, is_only_favorite)

    def draw_ref_cards(self, food_type: FoodType, is_only_favorite=False):
        ref_cards = self.get_ref_cards_by_food_type(food_type)

        if is_only_favorite:
            ref_cards = [i for i in ref_cards if i.ref_data.is_favorite == True]

        if not ref_cards:
            print(f"{food_type.value}에 해당하는 재료가 없습니다.")
            return

        scroll_area_content = None
        match food_type:
            case FoodType.MEAT:
                scroll_area_content = self.window.meat_scroll_area_content
            case FoodType.SEA_FOOD:
                scroll_area_content = self.window.sea_food_scroll_area_content
            case FoodType.FRUIT_VEGETABLE:
                scroll_area_content = self.window.fruit_vegetable_scroll_area_content
            case FoodType.OTHER:
                scroll_area_content = self.window.other_scroll_area_content

        if not scroll_area_content:
            print(f"{food_type.value} 스크롤 영역을 찾을 수 없습니다.")
            return

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
                card = RefCard(i.ref_data)

                ref_cards.append(card)

        return ref_cards

    def setup_sort_btn(self):
        from .sort_combo_box import setup_ui

        setup_ui(self.window.meat_sort_btn)
        setup_ui(self.window.sea_food_sort_btn)
        setup_ui(self.window.fruit_vegetable_sort_btn)
        setup_ui(self.window.other_sort_btn)

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
        widget = self.window.findChild(QGroupBox, f"{widget}")

        if not widget:
            print("위젯이 없습니다.")
            return

        widget.setVisible(True)
        end_rect = widget.geometry()
        start_rect = QRect(start_x, start_y, 27, 1)

        widget.setGeometry(start_rect)

        anim = QPropertyAnimation(widget, b"geometry")
        anim.setDuration(300)
        anim.setStartValue(start_rect)
        anim.setEndValue(end_rect)
        anim.start()
        widget._popup_anim = anim

    def toggle_button_by_lineedit(self):
        lineedit = self.window.findChild(QLineEdit, "recipe_search_box")
        button = self.window.findChild(QPushButton, "X_recipe_btn")
        if lineedit and button:
            if lineedit.text().strip():
                button.setVisible(True)
            else:
                button.setVisible(False)



    def get_all_ref_cards(self):
        refs = cs_db.Database.get_all()

        ref_cards = []
        for i in refs:
            card = RefCard(i)
            ref_cards.append(card)

        self.all_ref_cards = ref_cards

    def show_only_favorite(self):
        if self.is_show_only_favorite:
            self.is_show_only_favorite = False
            self.window.fav_ch_btn.setText("즐겨찾는 재료")

        else:
            self.is_show_only_favorite = True
            self.window.fav_ch_btn.setText("X")

        if self.is_show_only_favorite:
            self.draw_all_ref_cards(is_only_favorite=True)
        else:
            self.draw_all_ref_cards(is_only_favorite=False)

    def close_add_ref_modal(self, only_clear=False):
        self.add_ref_modal.name_line_edit.clear()
        self.add_ref_modal.amount_line_edit.clear()
        self.add_ref_modal.expiration_duration_date_edit.setDate(QDate.currentDate())
        self.add_ref_modal.type_combo_box.setCurrentIndex(0)

        if not only_clear:
            self.add_ref_modal.close()
