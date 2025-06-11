from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSizePolicy

class RecommandFeedBox(QFrame):
    def __init__(self, title_label, img, parent=None):
        super().__init__(parent)
        self.setObjectName("recommand_feed_box")
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setup_ui(title_label, img)

    def setup_ui(self, title_label, img):
        self.setFixedSize(150, 200)  # QFrame(자기 자신)에 크기 지정
        main_layout = QVBoxLayout(self)
        sub_v_layout = QVBoxLayout()
        sub_sub_h_layout = QHBoxLayout()
        sub_v_layout.setContentsMargins(0, 0, 0, 0)
        sub_v_layout.setAlignment(Qt.AlignCenter)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(2)
        main_layout.addWidget(self.create_button("imb_btn", " ", 120, 150, img))
        main_layout.addLayout(sub_v_layout)  # ← 여기만 addLayout으로 변경!
        sub_v_layout.addLayout(sub_sub_h_layout)
        sub_sub_h_layout.addWidget(self.set_label(title_label))
        sub_sub_h_layout.addWidget(self.add_horizontal_spacer(10))
        sub_sub_h_layout.addWidget(self.create_button("thumbs_up_btn", "👍", 24, 28, None))
        sub_sub_h_layout.addWidget(self.create_button("thumbs_down_btn", "👎", 24, 28, None))


    def create_button(self, name, text, size_hight, size_width, img):
        button = QPushButton(name)
        button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        if img:
            button.setStyleSheet(f"""
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
        label.setStyleSheet("font-size: 15px;")
        return label

    def add_horizontal_spacer(self, size_width):
        spacer = QFrame()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        spacer.setFixedWidth(size_width)
        return spacer
