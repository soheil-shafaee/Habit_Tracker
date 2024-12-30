from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
import sys
from user.login import Login


class SecondPage(QMainWindow):
    """
    This class display second page of wellcome, that go to login window, when
    user click on login Button.
    Attributes:
        login(QPushButton): That send user to login page.
    Method:
        using login function that go to Login class."""
    def __init__(self):
        super(QMainWindow, self).__init__()

        """Load The UI File"""
        uic.loadUi("second_page.ui", self)
        self.setFixedSize(436, 579)

        """Define Variable For using Class"""
        self.login_page = None

        """Define our Widgets"""
        self.login = self.findChild(QPushButton, "login_button")

        """Do Action with our widgets"""
        self.login.clicked.connect(self.login_user)

        """Show The Main Window"""
        self.show()

    def login_user(self):
        """Function For going to Login"""
        self.login_page = Login()
        self.login_page.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Second_Ui = SecondPage()
    app.exec_()
