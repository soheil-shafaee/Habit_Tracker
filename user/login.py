from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QCommandLinkButton, QMessageBox
from PyQt5 import uic, QtGui
import sys

from .signup import SignUp
from graph.choose_graph import ChooseGraph
from database.database import Users, session
from .token_hashing import hashing_password


class Login(QMainWindow):
    """This class represents the login window of the application. It handles user authentication,
    provides navigation to the registration window, and manages the visibility of the password field.

    Attributes:
        signup (SignUp): An instance of the SignUp class for user registration.
        choose_graph (ChooseGraph): An instance of the ChooseGraph class for navigating to the graph section.
        login_button (QPushButton): The button to initiate the login process.
        link_register (QCommandLinkButton): The button to navigate to the registration window.
        username_login (QLineEdit): The input field for the username.
        password_login (QLineEdit): The input field for the password.
        hide_show_password (QPushButton): The button to toggle password visibility.

    Methods:
        __init__(): Initializes the login window, loads the UI, and sets up the widgets.
        register(): Navigates to the registration window.
        graph_section(): Authenticates the user and navigates to the graph section upon successful login.
        visibility_password(): Toggles the visibility of the password input field."""
    def __init__(self):
        super(QMainWindow, self).__init__()

        """Load The UI File"""
        uic.loadUi("login.ui", self)
        self.setFixedSize(436, 579)

        """Define Variable For using Class"""
        self.signup = None
        self.choose_graph = None

        """Define our widgets"""
        self.login_button = self.findChild(QPushButton, "login")
        self.link_register = self.findChild(QCommandLinkButton, "register_2")
        self.username_login = self.findChild(QLineEdit, "username")
        self.password_login = self.findChild(QLineEdit, "password")
        self.hide_show_password = self.findChild(QPushButton, "hide_show")

        """Do Action with our widgets"""
        self.login_button.clicked.connect(self.graph_section)
        self.link_register.clicked.connect(self.register)
        self.hide_show_password.clicked.connect(self.visibility_password)

        """Show The Main Window"""
        self.show()

    def register(self):
        """Function For Create Account"""
        self.signup = SignUp()
        self.signup.show()
        self.close()

    def graph_section(self):
        """Function For login"""
        msg_login = QMessageBox()
        msg_login.setWindowIcon(QtGui.QIcon("../images/monster.png"))
        msg_login.setIcon(QMessageBox.Critical)
        if len(self.username_login.text()) == 0 or len(self.password_login.text()) == 0:
            msg_login.setWindowTitle("Field Empty")
            msg_login.setText("Fields cannot be left blank")
            msg_login.exec_()
            return
        user = session.query(Users).filter(Users.username == self.username_login.text()).first()
        if user is None:
            msg_login.setWindowTitle("User Not found")
            msg_login.setText("This user is not exist")
            msg_login.exec_()
            return

        client_password = hashing_password(self.password_login.text())
        if client_password != user.token:
            msg_login.setWindowTitle("Got Problem")
            msg_login.setText("Username Or Password are wrong!!")
            msg_login.exec_()
            return

        self.choose_graph = ChooseGraph(user.id)
        self.choose_graph.show()
        self.close()

    def visibility_password(self):
        if self.password_login.echoMode() == QLineEdit.Normal:
            self.password_login.setEchoMode(QLineEdit.Password)
        else:
            self.password_login.setEchoMode(QLineEdit.Normal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_Ui = Login()
    app.exec_()
