from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt5 import uic
import sys
from create_graph import CreateGraph


class SignUp(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.loadUi("create_account.ui", self)

        self.setFixedSize(436, 579)

        self.graph = None

        self.signup_button = self.findChild(QPushButton, "signup")

        self.signup_button.clicked.connect(self.create_new_user)

        self.show()

    def create_new_user(self):
        self.graph = CreateGraph()
        self.graph.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    signUp_View = SignUp()
    app.exec_()
