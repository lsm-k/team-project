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
    HELP = 2
    SETTING = 3


class RecipeTabKind(Enum):
    MAIN = 0
    BEEF = 1
    FISHES = 2
    VEGETABLE = 3
    ANOTHER = 4
    TAB = 5


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
        self.window.show_help_btn.clicked.connect(
            lambda: self.change_tab(self.window.tab_root, TabKind.HELP)
        )
        self.window.setting_btn.clicked.connect(
            lambda: self.change_tab(self.window.tab_root, TabKind.SETTING)
        )

        self.window.fav_ch_btn.clicked.connect(self.show_only_favorite)

        # ref add btns
        self.window.ref_add_self_btn.clicked.connect(self.show_add_ref_modal)

        self.add_ref_modal.yes_or_no_btn.accepted.connect(self.ok_ref_modal)
        self.add_ref_modal.yes_or_no_btn.rejected.connect(self.close_ref_modal)

        self.window.open_search_manage_modal_btn.clicked.connect(
            self.show_search_manage_ref_modal
        )

        self.search_manage_ref_modal.search_btn.clicked.connect(self.search_ref_manage)

        self.search_manage_ref_modal.name_edit.returnPressed.connect(
            self.search_ref_manage
        )  # 엔터키 누르면 검색

        # 재료페이지 검색 상자 오픈 버튼
        for i in range(1, 5):
            search_frame_num = self.window.findChild(
                QPushButton, f"show_search_box_btn_{i}"
            )
            if search_frame_num:
                search_frame_num.clicked.connect(
                    lambda checked=False, num=i: self.animation_search_box(
                        f"search_frame_{num}"
                    )
                )

        # 재료페이지 검색 버튼들
        from interface.interface_main import FoodType

        self.window.ref_meat_search_btn.clicked.connect(
            lambda: self.search_ref_by_name(food_type=FoodType.MEAT)
        )
        self.window.ref_fruit_vegetable_search_btn.clicked.connect(
            lambda: self.search_ref_by_name(food_type=FoodType.FRUIT_VEGETABLE)
        )
        self.window.ref_sea_food_search_btn.clicked.connect(
            lambda: self.search_ref_by_name(food_type=FoodType.SEA_FOOD)
        )
        self.window.ref_other_search_btn.clicked.connect(
            lambda: self.search_ref_by_name(food_type=FoodType.OTHER)
        )

        self.window.recipe_meat_btn.clicked.connect(
            lambda: self.change_tab_recipe(RecipeTabKind.BEEF)
        )

        self.window.recipe_meat_btn.clicked.connect(
            lambda: self.popup_animation_from_point("meat_tab_frame", 40, 30)
        )

        self.window.recipe_fishes_btn.clicked.connect(
            lambda: self.change_tab_recipe(RecipeTabKind.FISHES)
        )

        self.window.recipe_fishes_btn.clicked.connect(
            lambda: self.popup_animation_from_point("fishes_tab_frame", 170, 30)
        )

        self.window.recipe_vegetable_btn.clicked.connect(
            lambda: self.change_tab_recipe(RecipeTabKind.VEGETABLE)
        )

        self.window.recipe_vegetable_btn.clicked.connect(
            lambda: self.popup_animation_from_point("vegetable_tab_frame", 270, 30)
        )

        self.window.recipe_others_btn.clicked.connect(
            lambda: self.change_tab_recipe(RecipeTabKind.ANOTHER)
        )

        self.window.recipe_others_btn.clicked.connect(
            lambda: self.popup_animation_from_point("others_tab_frame", 400, 30)
        )

        self.window.X_recipe_btn.clicked.connect(self.clear_line_edit)

        self.window.return_meat_tab_btn.clicked.connect(
            lambda: self.change_tab_recipe(RecipeTabKind.MAIN)
        )

        self.window.return_others_tab_btn.clicked.connect(
            lambda: self.change_tab_recipe(RecipeTabKind.MAIN)
        )

        self.window.return_vegetable_tab_btn.clicked.connect(
            lambda: self.change_tab_recipe(RecipeTabKind.MAIN)
        )

        self.window.return_fishes_tab_btn.clicked.connect(
            lambda: self.change_tab_recipe(RecipeTabKind.MAIN)
        )

        self.window.my_own_recip_btn.clicked.connect(self.toggle_favorite_recipe)

        self.add_favorite_recipe_group_modal.yes_or_no_btn.accepted.connect(
            self.ok_add_favorite_recipe_group_modal
        )
        self.add_favorite_recipe_group_modal.yes_or_no_btn.rejected.connect(
            self.close_add_favorite_recipe_group_modal
        )

        # help page navigation
        self.window.help_next_btn.clicked.connect(self.next_help_page)
        self.window.help_prev_btn.clicked.connect(self.prev_help_page)

        self.window.recommand_feed_setting_btn.clicked.connect(self.recipe_search_by_ingredients)

        self.window.data_reset_btn.clicked.connect(self.reset_data)
