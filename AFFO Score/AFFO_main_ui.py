from PyQt6 import QtWidgets, uic, QtGui


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/Nuttapon/OneDrive/Desktop/G@nn3/Not a game/QT/AFFO_main_window.ui", self)
        self.setWindowTitle("AFFO Score")
        self.setWindowIcon(QtGui.QIcon("C:/Users/Nuttapon/OneDrive/Desktop/G@nn3/PICPIC/AFFO_icon.png"))

