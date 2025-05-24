# import warnings
# warnings.filterwarnings('ignore', category=DeprecationWarning)

import sys
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QApplication
from PySide6.QtCore import Qt, QEvent, QMimeData
from PySide6.QtGui import QDrag


class IndicSelectWindow(QWidget):
    def __init__(self, parent=None):
        super(IndicSelectWindow, self).__init__(parent=parent)
        self.resize(1000, 800)

        self.target = None
        self.setAcceptDrops(True)
        self.gridLayout = QGridLayout(self)

        for i in range(4):
            for j in range(4):
                self.label_test = QLabel(f'Label_{i+1}-{j+1}')
                self.label_test.setStyleSheet('background-color: black; color: white; font: 26pt')

                Box = QVBoxLayout()
                Box.addWidget(self.label_test)
                self.gridLayout.addLayout(Box, i, j)

    def eventFilter(self, watched, event):
        if event.type() == QEvent.MouseButtonPress:
            self.mousePressEvent(event)
        elif event.type() == QEvent.MouseMove:
            self.mouseMoveEvent(event)
        elif event.type() == QEvent.MouseButtonRelease:
            self.mouseReleaseEvent(event)
        return super().eventFilter(watched, event)

    def get_index(self, pos):
        for i in range(self.gridLayout.count()):
            if self.gridLayout.itemAt(i).geometry().contains(pos) and i != self.target:
                return i

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.target = self.get_index(event.windowPos().toPoint())
        else:
            self.target = None

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.target is not None:
            drag = QDrag(self.gridLayout.itemAt(self.target))
            pix = self.gridLayout.itemAt(self.target).itemAt(0).widget().grab()
            mimedata = QMimeData()
            mimedata.setImageData(pix)
            drag.setMimeData(mimedata)
            drag.setPixmap(pix)
            drag.exec()

    def mouseReleaseEvent(self, event):
        self.target = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if not event.source().geometry().contains(event.pos()):
            source = self.get_index(event.pos())
            if source is None:
                return

            i, j = max(self.target, source), min(self.target, source)
            p1, p2 = self.gridLayout.getItemPosition(i), self.gridLayout.getItemPosition(j)

            self.gridLayout.addItem(self.gridLayout.takeAt(i), *p2)
            self.gridLayout.addItem(self.gridLayout.takeAt(j), *p1)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F:
            self.showFullScreen()

        if event.key() == Qt.Key_D:
            self.showNormal()

        if event.modifiers() & Qt.ControlModifier:
            if event.key() == Qt.Key_W:
                self.close()
                sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = IndicSelectWindow()
    w.show()
    sys.exit(app.exec())