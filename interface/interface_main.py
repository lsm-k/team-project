import sys
import os
from PySide6.QtWidgets import QApplication, QTextBrowser, QWidget, QGridLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QMimeData, QByteArray, QDataStream, QIODevice
from PySide6.QtGui import QDrag, QPixmap, QPainter

from enum import Enum


class TabKind(Enum):
    STORAGE_STATUS = 0
    RECIPE = 1
    RECOMMEND = 2
    SETTING = 3


class DraggableTextBrowser(QTextBrowser):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self._drag_start_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_start_pos = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if (
            event.buttons() & Qt.LeftButton
            and self._drag_start_pos is not None
            and (event.pos() - self._drag_start_pos).manhattanLength() > QApplication.startDragDistance()
        ):
            drag = QDrag(self)
            mime_data = QMimeData()
            if not self.objectName():
                self.setObjectName(f"DraggableTextBrowser_{id(self)}")
            mime_data.setData("application/x-qwidget-objectname", self.objectName().encode())
            pixmap = self.grab()
            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.setMimeData(mime_data)
            drag.exec(Qt.MoveAction)
        else:
            super().mouseMoveEvent(event)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-qwidget-objectname"):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("application/x-qwidget-objectname"):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasFormat("application/x-qwidget-objectname"):
            src_object_name = event.mimeData().data("application/x-qwidget-objectname").data().decode()
            src_widget = self.parent().findChild(QTextBrowser, src_object_name)
            if src_widget and src_widget is not self:
                parent_layout = self.parent().layout()
                if isinstance(parent_layout, QGridLayout):
                    pos_self = None
                    pos_src = None
                    for row in range(parent_layout.rowCount()):
                        for col in range(parent_layout.columnCount()):
                            item = parent_layout.itemAtPosition(row, col)
                            if item and item.widget() is self:
                                pos_self = (row, col)
                            if item and item.widget() is src_widget:
                                pos_src = (row, col)
                    if pos_self and pos_src:
                        parent_layout.removeWidget(self)
                        parent_layout.removeWidget(src_widget)
                        self.setParent(None)
                        src_widget.setParent(None)
                        parent_layout.addWidget(self, *pos_src)
                        parent_layout.addWidget(src_widget, *pos_self)
                event.acceptProposedAction()
            else:
                event.ignore()
        else:
            event.ignore()


class Mainwindow:
    window = None

    def load_ui(self):
        ui_file = QFile(os.path.join(os.path.dirname(__file__), "material_stat.ui"))
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        window = loader.load(ui_file)
        ui_file.close()

        self.window = window
        
        for widget in self.window.findChildren(QWidget):
            if widget.objectName().startswith("widget_"):
                layout = widget.layout()
                if isinstance(layout, QGridLayout):
                    for row in range(layout.rowCount()):
                        for col in range(layout.columnCount()):
                            item = layout.itemAtPosition(row, col)
                            if item:
                                child = item.widget()
                                if isinstance(child, QTextBrowser) and not isinstance(child, DraggableTextBrowser):
                                    text = child.toPlainText()
                                    layout.removeWidget(child)
                                    child.deleteLater()
                                    new_tb = DraggableTextBrowser()
                                    new_tb.setPlainText(text)
                                    layout.addWidget(new_tb, row, col)

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