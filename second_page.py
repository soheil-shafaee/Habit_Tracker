from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
import sys
from login import Login

class SecondPage(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.loadUi("second_page.ui", self)

        self.setFixedSize(436, 579)

        self.login = self.findChild(QPushButton, "login_button")

        self.login_page = None

        self.login.clicked.connect(self.login_user)

        self.show()

    def login_user(self):
        self.login_page = Login()
        self.login_page.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Second_Ui = SecondPage()
    app.exec_()
