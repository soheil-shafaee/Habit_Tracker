from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QCommandLinkButton, QMessageBox
from PyQt5 import uic
import sys
from signup import SignUp
from add_pixel import AddPixel
import psycopg2

# ----------- DataBase Section --------
try:
    conx_add_graph = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="8VMNKEZlg%",
        database="habit_tracker",

    )

    cur = conx_add_graph.cursor()
    com_users = """SELECT username, token FROM users"""
    cur.execute(com_users)
    users = cur.fetchall()


except Exception as e:
    print(e)


class Login(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.loadUi("login.ui", self)

        self.setFixedSize(436, 579)

        self.signup = None
        self.go_add_pixel = None

        """Define our widgets"""
        self.login_button = self.findChild(QPushButton, "login")
        self.link_register = self.findChild(QCommandLinkButton, "register_2")
        self.username_login = self.findChild(QLineEdit, "username")
        self.password_login = self.findChild(QLineEdit, "password")

        self.login_button.clicked.connect(self.into_add_pixel)
        self.link_register.clicked.connect(self.register)

        self.show()

    def register(self):
        self.signup = SignUp()
        self.signup.show()
        self.close()

    def into_add_pixel(self):
        if self.username_login.text() == users[0][0] and self.password_login.text() == users[0][1]:
            self.go_add_pixel = AddPixel()
            self.go_add_pixel.show()
            self.close()
        else:
            msg_login = QMessageBox()
            msg_login.setWindowTitle("User Not found")
            msg_login.setText("This user is not exist")
            msg_login.setIcon(QMessageBox.Warning)
            msg_login.exec_()


if __name__ == "__main":
    app = QApplication(sys.argv)
    login_Ui = Login()
    app.exec_()
