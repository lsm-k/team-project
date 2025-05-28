from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QToolButton,
    QMenu,
    QLabel,
    QListWidget,
    QListWidgetItem,
)


def setup_ui(tool_btn):
    combo_box = FocusComboBox()
    combo_box.addItems(
        [
            "이름 오름차순",
            "이름 내림차순",
            "날짜 오름차순",
            "날짜 내림차순",
            "크기 오름차순",
            "크기 내림차순",
        ]
    )
    combo_box.setVisible(False)
    combo_box.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    tool_btn.clicked.connect(lambda: combo_box.toggle_combo_box(tool_btn))


from PySide6.QtCore import QTimer


class FocusComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.currentTextChanged.connect(self.on_combo_changed)
        self.setup_timer()

    def setup_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.visible_false)
        self.timer.start(5000)

    def visible_false(self):
        if self.focusWidget() == self:
            self.setVisible(False)

    def toggle_combo_box(self, btn):
        self.setVisible(not self.isVisible())
        if self.isVisible():

            button_bottom = btn.mapToGlobal(btn.rect().bottomLeft())

            combo_x = button_bottom.x()
            combo_y = button_bottom.y() + 5

            self.setGeometry(combo_x, combo_y, self.width(), 25)

            self.showPopup()

    def on_combo_changed(self):
        self.setVisible(False)
