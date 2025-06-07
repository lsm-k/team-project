from PySide6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFrame,
    QLabel,
    QPushButton,
    QScrollArea,
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QPalette

from cold_storage import db as cs_db


class RefCard(QFrame):
    def __init__(
        self, ref, delete_callback=None, edit_callback=None, favorite_callback=None
    ):
        super().__init__()
        self.ref_data = ref
        self.delete_callback = delete_callback
        self.edit_callback = edit_callback
        self.favorite_callback = favorite_callback

        self.setup_ui()
        self.setup_style()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

        header_layout = QHBoxLayout()

        self.name_label = QLabel(self.ref_data.Food_name)
        # self.name_label.setFont(QFont("맑은 고딕", 14, QFont.Bold))
        # self.name_label.setWordWrap(True)

        self.favorite_btn = QPushButton()
        self.update_favorite_button()
        self.favorite_btn.setFixedSize(32, 32)
        self.favorite_btn.clicked.connect(self.toggle_favorite)

        header_layout.addWidget(self.name_label)
        header_layout.addStretch()
        header_layout.addWidget(self.favorite_btn)

        info_layout = QVBoxLayout()
        info_layout.setSpacing(8)

        # 수량
        quantity_layout = self.create_info_row("수량", str(self.ref_data.Amount))
        info_layout.addLayout(quantity_layout)

        # 소비기한
        expiry_layout = self.create_info_row("소비기한", self.ref_data.Expiration_date)
        info_layout.addLayout(expiry_layout)

        # 액션 버튼들
        action_layout = QHBoxLayout()
        action_layout.addStretch()

        edit_btn = QPushButton("수정")
        edit_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #3b82f6;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
            QPushButton:pressed {
                background-color: #1d4ed8;
            }
        """
        )

        delete_btn = QPushButton("삭제")
        delete_btn.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: #6b7280;
                border: 1px solid #d1d5db;
                padding: 6px 12px;
                border-radius: 4px;
                font-size: 11px;
            }
            QPushButton:hover {
                border-color: #9ca3af;
                color: #374151;
            }
            QPushButton:pressed {
                background-color: #f3f4f6;
            }
        """
        )

        delete_btn.clicked.connect(self.delete)

        edit_btn.clicked.connect(self.edit)

        action_layout.addWidget(edit_btn)
        action_layout.addWidget(delete_btn)

        main_layout.addLayout(header_layout)
        main_layout.addLayout(info_layout)
        main_layout.addStretch()
        main_layout.addLayout(action_layout)

    def delete(self):
        self.delete_callback(self.ref_data.id)

    def edit(self):
        print("Edit button clicked")
        self.edit_callback(self.ref_data)

    def favorite_func(self):
        self.favorite_callback(self.ref_data.id, self.ref_data.Food_type, self.ref_data.is_favorite)

    def create_info_row(self, label_text, value_text):
        layout = QHBoxLayout()

        label = QLabel(label_text)
        # label.setFont(QFont("맑은 고딕", 10))
        # label.setStyleSheet("color: #666;")

        value = QLabel(value_text)
        # value.setFont(QFont("맑은 고딕", 10, QFont.Bold))
        value.setAlignment(Qt.AlignRight)

        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(value)

        return layout

    def update_favorite_button(self):
        if self.ref_data.is_favorite:
            self.favorite_btn.setText("❤️")
            self.favorite_btn.setStyleSheet(
                """
                QPushButton {
                    border: none;
                    background: transparent;
                    font-size: 18px;
                }
            """
            )
        else:
            self.favorite_btn.setText("🤍")
            self.favorite_btn.setStyleSheet(
                """
                QPushButton {
                    border: none;
                    background: transparent;
                    font-size: 18px;
                }
            """
            )

    def set_favorite(self, is_favorite: bool):
        self.ref_data.is_favorite = is_favorite
        self.update_favorite_button()

    def toggle_favorite(self):
        if self.ref_data.is_favorite:
            self.unfavorite(self.ref_data.id)
        else:
            self.favorite(self.ref_data.id)

        self.ref_data.is_favorite = not self.ref_data.is_favorite
        self.favorite_func()
        self.update_favorite_button()
        print(f"{self.ref_data.Food_name} 즐겨찾기: {self.ref_data.is_favorite}")

    def setup_style(self):
        self.setFrameStyle(QFrame.Box)
        self.setStyleSheet(
            """
            refCard {
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                margin: 4px;
            }
            refCard:hover {
                border-color: #d1d5db;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }
        """
        )
        # self.setFixedWidth(280)
        # self.setFixedHeight(200)

    def favorite(self, id: int):
        cs_db.Database.update_favorite(self.ref_data.id, True)

    def unfavorite(self, id: int):
        cs_db.Database.update_favorite(self.ref_data.id, False)
