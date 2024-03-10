from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt5 import uic
import sys


class AddPixel(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.loadUi("add_pixel.ui", self)

        self.setFixedSize(436, 579)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    add_pixel = AddPixel()
    app.exec_()
