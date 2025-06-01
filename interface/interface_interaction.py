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
    QPushButton,
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


class TabKind(Enum):
    STORAGE_STATUS = 0
    RECIPE = 1
    RECOMMEND = 2
    SETTING = 3
    REF_ADD_SELF = 4
    REF_ADD_IMAGE = 5


class InterfaceInteraction:
    window = None
    add_ref_modal = None
    search_manage_ref_modal = None

    def setup_ui(self):
        self.window = self.load_ui("material_stat")
        self.add_ref_modal = self.load_ui("add_ref_modal")
        self.search_manage_ref_modal = self.load_ui("search_manage_ref_modal")

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

        self.search_manage_ref_modal.name_edit.returnPressed.connect(self.search_ref_manage)        #엔터키 누르면 검색

        # self.window.show_search_box_btn_1.clicked.connect(
        #     lambda: self.animation_search_box("search_frame_1")
        # )

        # self.window.show_search_box_btn_2.clicked.connect(
        #     lambda: self.animation_search_box("search_frame_2")
        # )

        # self.window.show_search_box_btn_3.clicked.connect(
        #     lambda: self.animation_search_box("search_frame_3")
        # )

        # self.window.show_search_box_btn_4.clicked.connect(
        #     lambda: self.animation_search_box("search_frame_4")
        # )

        for i in range (1,5):
            search_frame_num = self.window.findChild(QPushButton, f"show_search_box_btn_{i}")
            if search_frame_num:
                search_frame_num.clicked.connect(
                    lambda checked = False, num=i: self.animation_search_box(f"search_frame_{num}")
                )
