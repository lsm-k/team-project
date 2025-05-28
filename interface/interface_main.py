import sys
import os
from enum import Enum

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QTextBrowser,
    QComboBox,
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QMimeData, QCoreApplication, QUrl
from PySide6.QtGui import QDrag, QPixmap, QPainter
from PySide6.QtWebEngineWidgets import QWebEngineView

from cold_storage import db as cs_db


class FoodType(Enum):
    FRUIT_VEGETABLE = "과일 & 채소"
    MEAT = "육류"
    SEA_FOOD = "어류"
    OTHER = "기타"


class TabKind(Enum):
    STORAGE_STATUS = 0
    RECIPE = 1
    RECOMMEND = 2
    SETTING = 3
    REF_ADD_SELF = 4
    REF_ADD_IMAGE = 5


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

    def display_none_all_tabs(self):
        tab_cnt = self.window.tab_root.count()
        for i in range(0, tab_cnt):
            self.window.tab_root.setTabVisible(i, False)

    def setting_events(self):
        # side bar btns
        self.window.storage_status_btn.clicked.connect(
            lambda: self.change_tab(self.window.tab_root, TabKind.STORAGE_STATUS)
        )
        self.window.recipe_btn.clicked.connect(
            lambda: self.change_tab(self.window.tab_root, TabKind.RECIPE)
        )
        self.window.recommend_btn.clicked.connect(
            lambda: self.change_tab(self.window.tab_root, TabKind.RECOMMEND)
        )
        self.window.setting_btn.clicked.connect(
            lambda: self.change_tab(self.window.tab_root, TabKind.SETTING)
        )

        # self.window.fav_ch_btn.clicked.connect(
        #     lambda: self.change_tab(self.window.ref_tab_widget, TabKind_nomal.NOMAL)
        # )

        # ref add btns
        self.window.ref_add_self_btn.clicked.connect(self.show_add_ref_modal)

        self.window.open_search_manage_modal_btn.clicked.connect(
            self.show_search_manage_ref_modal
        )
        self.search_manage_ref_modal.search_btn.clicked.connect(self.search_ref_manage)

        # self.add_ref_modal.buttonBox.connected(show_add_ref_modal)

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

        self.setting_events()

        self.display_none_all_tabs()
        self.window.tab_root.setCurrentIndex(TabKind.STORAGE_STATUS.value)

        self.setup_combo_box()
        self.setup_sort_btn()

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
        search_text = self.search_manage_ref_modal.name_edit.text() + " 관리 방법"

        self.search_manage_ref_modal.youtube_view.load(QUrl(f"https://www.youtube.com/results?search_query={search_text}"))
        self.search_manage_ref_modal.google_view.load(QUrl(f"https://www.google.com/search?q={search_text}"))



    def change_tab(self, tab_widget, tab_kind):
        tab_widget.setCurrentIndex(tab_kind.value)
        print(f"Changed tab to {tab_kind.value} ({tab_kind.name})")

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
