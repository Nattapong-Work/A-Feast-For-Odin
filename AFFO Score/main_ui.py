import sys
from PyQt6 import QtWidgets, uic


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/Nuttapon/OneDrive/Desktop/G@nn3/Not a game/QT/AFFO_main_window.ui", self)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())