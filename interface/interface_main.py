import sys
import os
from PyQt6 import QtWidgets, uic

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui_file = os.path.join(os.path.dirname(__file__), "interface_ui.ui")
    window = uic.loadUi(ui_file)
    window.show()
    sys.exit(app.exec())