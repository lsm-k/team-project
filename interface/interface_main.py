import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from enum import Enum


class TabKind(Enum):
    STORAGE_STATUS = 0
    RECIPE = 1
    RECOMMEND = 2
    SETTING = 3


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

    def show(self):
        app = QApplication(sys.argv)

        self.load_ui()
        self.setting_events()
        self.display_none_all_tabs()
        self.window.tab_root.setCurrentIndex(TabKind.STORAGE_STATUS.value)

        self.window.show()

        sys.exit(app.exec())

    def change_tab(self, tab_kind):
        self.window.tab_root.setCurrentIndex(tab_kind.value)
