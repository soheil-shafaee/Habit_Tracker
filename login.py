from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QCommandLinkButton
from PyQt5 import uic
import sys
from signup import SignUp
from add_pixel import AddPixel


class Login(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.loadUi("login.ui", self)

        self.setFixedSize(436, 579)

        self.signup = None
        self.go_add_pixel = None

        self.login_button = self.findChild(QPushButton, "login")
        self.link_register = self.findChild(QCommandLinkButton, "register_2")

        self.login_button.clicked.connect(self.into_add_pixel)
        self.link_register.clicked.connect(self.register)

        self.show()

    def register(self):
        self.signup = SignUp()
        self.signup.show()
        self.close()

    def into_add_pixel(self):
        self.go_add_pixel = AddPixel()
        self.go_add_pixel.show()
        self.close()


if __name__ == "__main":
    app = QApplication(sys.argv)
    login_Ui = Login()
    app.exec_()
