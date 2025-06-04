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
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
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
from interface.interface_interaction import InterfaceInteraction, TabKind

class ref_group_box(QWidget):  # QWidget 상속 추가
    def __init__(self, title="", parent=None):
        super().__init__(parent)  # parent 전달
        self.setAcceptDrops(False)
        self._drag_start_pos = None
        self.setFixedSize(213, 110)  # 너비 213, 높이 110으로 고정

        # 메인 레이아웃
        main_layout = QVBoxLayout(self)

        # 가운데: 텍스트박스 + (오른쪽에 버튼 2개 세로)
        h_layout = QHBoxLayout()
        self.text_browser = QTextBrowser()
        self.text_browser.setFixedSize(155, 90)  # 텍스트박스 크기 고정
        h_layout.addWidget(self.text_browser)
        self.text_browser.setMinimumSize(155, 90)

        
        main_layout.addLayout(h_layout)  # ★ 이 줄을 꼭 추가하세요!