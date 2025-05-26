import sys
import os
from enum import Enum

from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QTextBrowser
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QMimeData
from PySide6.QtGui import QDrag, QPixmap, QPainter

from database.cold_storage import db as cs_db


class FoodType(Enum):
    FRUIT = "과일"
    VEGETABLE = "채소"
    MEAT = "육류"
    FISH = "어류"
    DAIRY = "유제품"
    GRAIN = "곡류"
    PROCESSED = "가공식품"
    BEVERAGE = "음료수"
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

    def load_ui(self):
        ui_file = QFile(os.path.join(os.path.dirname(__file__), "material_stat.ui"))
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        window = loader.load(ui_file)
        ui_file.close()
        self.window = window

    def display_none_all_tabs(self):
        tab_cnt = self.window.tab_root.count()
        for i in range(0, tab_cnt):
            self.window.tab_root.setTabVisible(i, False)

    def setting_events(self):
        # side bar btns
        self.window.storage_status_btn.clicked.connect(
            lambda: self.change_tab(TabKind.STORAGE_STATUS)
        )
        self.window.recipe_btn.clicked.connect(lambda: self.change_tab(TabKind.RECIPE))
        self.window.recommend_btn.clicked.connect(
            lambda: self.change_tab(TabKind.RECOMMEND)
        )
        self.window.setting_btn.clicked.connect(
            lambda: self.change_tab(TabKind.SETTING)
        )

        # ref add btns
        self.window.ref_add_self_btn.clicked.connect(
            lambda: self.change_tab(TabKind.REF_ADD_SELF)
        )
        self.window.ref_add_image_btn.clicked.connect(
            lambda: self.change_tab(TabKind.REF_ADD_IMAGE)
        )

        # ref add self tab
        self.window.ref_add_self_ok_btn.clicked.connect(self.create_ref)
        self.window.ref_add_self_cancel_btn.clicked.connect(
            lambda: self.change_tab(TabKind.STORAGE_STATUS)
        )

    def setup_combo_box(self):
        self.window.type_combo_box.clear()
        lists = [i.value for i in FoodType]
        self.window.type_combo_box.addItems(lists)

    def show(self):
        app = QApplication(sys.argv)
        self.load_ui()
        self.setting_events()
        self.display_none_all_tabs()
        self.window.tab_root.setCurrentIndex(TabKind.STORAGE_STATUS.value)
        self.setup_combo_box()
        self.window.show()
        sys.exit(app.exec())

    def change_tab(self, tab_kind):
        self.window.tab_root.setCurrentIndex(tab_kind.value)

    # TODO: add validation, insert error handling
    def create_ref(self):
        food_name = self.window.name_line_edit.text()
        amount = self.window.amount_line_edit.text()
        expiration_date = self.window.expiration_duration_date_edit.text()
        food_type = self.window.type_combo_box.currentText()
        print(f"Creating ref: {food_name}, {amount}, {expiration_date}, {food_type}")

        cs_db.Database.data_insert(food_name, amount, expiration_date, food_type)

        self.change_tab(TabKind.STORAGE_STATUS)
