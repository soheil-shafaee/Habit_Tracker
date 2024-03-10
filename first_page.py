from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
import sys
from second_page import SecondPage


class FirstPage(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.loadUi("first_page.ui", self)

        self.setFixedSize(436, 579)
        self.second_page = None

        self.start = self.findChild(QPushButton, "start_button")

        self.start.clicked.connect(self.get_start)

        self.show()

    def get_start(self):
        self.second_page = SecondPage()
        self.second_page.show()
        self.close()


app = QApplication(sys.argv)
UI = FirstPage()
app.exec_()
