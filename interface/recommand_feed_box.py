from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
)

from recipe.db import Database as db


class RecommandFeedBox(QFrame):
    def __init__(
        self,
        recipe_id,
        title_label,
        img,
        parent=None,
        open_modal_callback=None,
    ):
        super().__init__(parent)

        self.recipe_id = recipe_id
        self.open_modal_callback = open_modal_callback
        self.setStyleSheet("""
                    QFrame#recommand_feed_box {
                           border-color: rgb(0, 0, 0);
                           border-width: 1px;
                           border-style: solid;
                           border-radus: 75px;
                           background-color: rgb(255, 255, 255, 0);
                           }
                           """)

        self.setObjectName("recommand_feed_box")
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setup_ui(title_label, img, recipe_id)

    def setup_ui(self, title_label, img, recipe_id):
        self.setFixedSize(150, 200)  # QFrame(자기 자신)에 크기 지정
        main_layout = QVBoxLayout(self)
        sub_v_layout = QVBoxLayout()
        sub_sub_h_layout = QHBoxLayout()
        sub_v_layout.setContentsMargins(0, 0, 0, 0)
        sub_v_layout.setAlignment(Qt.AlignCenter)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(2)
        img_btn = self.create_button("img_btn", " ", 120, 150, img)
        img_btn.clicked.connect(lambda: self.open_modal_callback(self.recipe_id))
        main_layout.addWidget(img_btn)
        main_layout.addLayout(sub_v_layout)  # ← 여기만 addLayout으로 변경!
        sub_v_layout.addWidget(self.set_label(title_label))
        sub_v_layout.addLayout(sub_sub_h_layout)
        sub_sub_h_layout.addWidget(
            thumbs_up_btn := self.create_button("thumbs_up_btn", "👍", 24, 42, None)
        )
        sub_sub_h_layout.addWidget(
            thumbs_down_btn := self.create_button("thumbs_down_btn", "👎", 24, 42, None)
        )
        
        thumbs_up_btn.clicked.connect(lambda: db.change_thumbs_up(recipe_id, 1))    # 1 = TRUE

        thumbs_down_btn.clicked.connect(lambda: db.change_thumbs_up(recipe_id, 0))  # 0 = FALSE

    def create_button(self, name, text, size_hight, size_width, img):
        button = QPushButton(name)
        button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        if img:
            button.setStyleSheet(
                f"""
                                 border-image:url({img});
                                 border:0px;
                                 """
            )
        button.setFixedSize(size_width, size_hight)
        button.setCursor(Qt.PointingHandCursor)
        button.setText(text)
        return button

    def set_label(self, title):
        label = QLabel(title)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 9px;")
        return label

    def open_modal(self, recipe_id):
        if self.open_modal_callback:
            print(f"Opening modal for recipe ID: {recipe_id}")
            self.open_modal_callback(recipe_id)
