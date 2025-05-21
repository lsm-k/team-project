import sys
import os
from PyQt6 import QtWidgets, uic

class Mainwindow():
    @classmethod
    def mainrun(cls):
        app = QtWidgets.QApplication(sys.argv)
        ui_file = os.path.join(os.path.dirname(__file__), "material_stat.ui")
        window = uic.loadUi(ui_file)
        window.show()
        sys.exit(app.exec())