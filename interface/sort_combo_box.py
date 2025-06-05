from enum import Enum

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

from interface.interface_main import FoodType, OrderingType

def setup_ui(tool_btn, food_type, callback_func=None):
    combo_box = FocusComboBox(food_type=food_type, callback_func=callback_func)

    lists = [i.value for i in OrderingType]
    combo_box.addItems(lists)

    combo_box.setVisible(False)
    combo_box.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    tool_btn.clicked.connect(lambda: combo_box.toggle_combo_box(tool_btn))


from PySide6.QtCore import QTimer


class FocusComboBox(QComboBox):
    def __init__(self, parent=None, food_type=FoodType, callback_func=None):
        super().__init__(parent)
        self.food_type = food_type
        self.callback_func = callback_func
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
        self.callback_func( self.food_type, self.currentText())
