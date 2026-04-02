import sys
from PyQt6 import QtWidgets
from AFFO_main_ui import MyWindow
import AFFO_Logic as logic


class AppController(MyWindow):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = AppController()
    controller.show()
    sys.exit(app.exec())