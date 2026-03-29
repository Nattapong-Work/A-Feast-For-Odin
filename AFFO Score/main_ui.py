import sys
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout


# window design
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AFFO Score")

        shipbox = QGridLayout(self) # layout

        whale_ship_bt = QPushButton("add") # button
        knarr_ship_bt = QPushButton("add")
        knarr_emi_bt  = QPushButton("add")
        long_ship_bt  = QPushButton("add")
        long_emi_bt   = QPushButton("add")

        whale_ship_lb = QLabel("whale ship")  # label
        knarr_ship_lb = QLabel("knarr ship")
        knarr_emi_lb  = QLabel("knarr emigration")
        long_ship_lb  = QLabel("longship")
        long_emi_lb   = QLabel("longship emigration")

        shipbox.addWidget(whale_ship_bt, 1, 0)# add but to the layout
        shipbox.addWidget(whale_ship_lb, 0, 0)

        shipbox.addWidget(knarr_ship_bt, 1, 1)
        shipbox.addWidget(knarr_ship_lb, 0, 1)

        shipbox.addWidget(knarr_emi_bt, 1, 2)
        shipbox.addWidget(knarr_emi_lb, 0, 2)


        shipbox.addWidget(long_ship_bt, 1, 3)
        shipbox.addWidget(long_ship_lb, 0, 3)


        shipbox.addWidget(long_emi_bt, 1, 4)
        shipbox.addWidget(long_emi_lb, 0, 4)

# program running
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()