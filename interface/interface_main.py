import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class Mainwindow:
    @classmethod
    def mainrun(cls):
        app = QApplication(sys.argv)

        ui_file = QFile(
            os.path.join(os.path.dirname(__file__), "material_stat.ui")
        )
        ui_file.open(QFile.ReadOnly)
        
        loader = QUiLoader()
        window = loader.load(ui_file)
        ui_file.close()

        window.show()

        sys.exit(app.exec())