from PyQt6 import QtWidgets, uic, QtGui


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("AFFO_src/AFFO_main_window.ui", self)
        self.setWindowTitle("AFFO Score")
        self.setWindowIcon(QtGui.QIcon("AFFO_src/AFFO_icon.png"))

