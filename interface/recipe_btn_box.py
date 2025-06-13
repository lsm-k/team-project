from PySide6.QtWidgets import QFrame, QCheckBox, QSizePolicy, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, Signal


class RecipeBtnBox(QFrame):
    checkedChanged = Signal(bool)

    def __init__(
        self, checkbox_name, parent=None, add_callback=None, remove_callback=None
    ):
        super().__init__(parent)
        self.setObjectName("recipe_btn_box")
        self.add_callback = add_callback
        self.remove_callback = remove_callback
        self.name = checkbox_name
        self.setStyleSheet(
            """
            QFrame#recipe_btn_box {
                min-width: 20px;
                min-height: 20px;
                border-color: rgb(0, 0, 0);
                border-width: 1px;
                border-style: solid;
                border-radius: 10px;
                background-color: rgb(255, 255, 255, 0);
            }
        """
        )
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)  # 크기 자동 맞춤
        # self.setFixedHeight(40)  # 이 줄은 제거!
        self.setup_ui(checkbox_name)

    def setup_ui(self, checkbox_name):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignCenter)

        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.setAlignment(Qt.AlignCenter)

        self.checkbox = self.create_checkbox(checkbox_name)
        h_layout.addWidget(self.checkbox)

        main_layout.addLayout(h_layout)

    def create_checkbox(self, text):
        cbox = QCheckBox(text)
        cbox.setSizePolicy(
            QSizePolicy.Maximum, QSizePolicy.Maximum
        )  # 체크박스 크기에 맞춤
        cbox.setStyleSheet("font-size: 16px;")
        cbox.stateChanged.connect(self.change_checkbox_state)
        return cbox

    def change_checkbox_state(self, state):
        # Qt.CheckState로 변환하여 사용
        check_state = Qt.CheckState(state)
        if check_state == Qt.CheckState.Checked:
            self.add_callback(self.name)
        elif check_state == Qt.CheckState.Unchecked:
            self.remove_callback(self.name)
