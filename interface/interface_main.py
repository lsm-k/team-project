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
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QDrag, QPixmap, QPainter
from PySide6.QtWebEngineWidgets import QWebEngineView

from cold_storage import db as cs_db
from interface.interface_interaction import InterfaceInteraction, TabKind, RecipeTabKind


class FoodType(Enum):
    FRUIT_VEGETABLE = "과일 & 채소"
    MEAT = "육류"
    SEA_FOOD = "어류"
    OTHER = "기타"

class Mainwindow:
    window = None
    add_ref_modal = None
    search_manage_ref_modal = None

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

    #set window button events
    def setup_combo_box(self):
        combo = self.window.findChild(QComboBox, "type_combo_box")
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

        self.ref_get_all()

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

        cs_db.Database.data_insert(food_name, amount, expiration_date, food_type)

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



    def ref_get_all(self):
        from interface.ref_card import RefCard
        from favorite_ref import db as favorite_db

        refs = cs_db.Database.get_all()
        fav_ref_ids = []
        for i in favorite_db.Database.get_all():
            fav_ref_ids.append(i.ref_id)

        for i in refs:
            card = RefCard(i)

            if i.id in fav_ref_ids:
                card.set_favorite(True)
            self.window.meat_scroll_area_content.layout().insertWidget(2, card)
