from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QRadioButton, QMessageBox
from PyQt5 import uic
import sys
from create_graph import CreateGraph
import psycopg2
from psycopg2.extras import RealDictCursor
import re

# ------- Database Section ---------
try:
    conx = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="8VMNKEZlg%",
        database="habit_tracker",
        cursor_factory=RealDictCursor

    )

    cur = conx.cursor()
    print("Database connect")
except Exception as e:
    print(e)


# ------- Validate Email Section -------
def validate_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False


# ----------- SignUp Section ----------

class SignUp(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.loadUi("create_account.ui", self)

        self.setFixedSize(436, 579)

        self.graph = None

        """Define our widgets"""
        self.signup_button = self.findChild(QPushButton, "signup")
        self.username_create = self.findChild(QLineEdit, "username")
        self.password_create = self.findChild(QLineEdit, "password")
        self.email_create = self.findChild(QLineEdit, "email")
        self.agree_terms_create = self.findChild(QRadioButton, "terms")

        """Do Action with our widgets"""
        self.signup_button.clicked.connect(self.create_new_user)

        """Display Window"""
        self.show()

    def create_new_user(self):
        name = self.username_create.text()
        token = self.password_create.text()
        email = self.email_create.text()
        if validate_email(email) and self.agree_terms_create.isChecked():
            try:
                cur.execute("""INSERT INTO users(username, token, email) VALUES(%s, %s, %s)""",
                            (name, token, email))
                conx.commit()
            except Exception as error:
                print(error)
                conx.rollback()

        # self.graph = CreateGraph()
        # self.graph.show()
        # self.close()
        elif not self.agree_terms_create.isChecked():
            msg_terms = QMessageBox()
            msg_terms.setWindowTitle("Please Read The terms of service")
            msg_terms.setText("Terms is not checked!!")
            msg_terms.setIcon(QMessageBox.Warning)
            msg_terms.exec_()

        else:
            msg_email = QMessageBox()
            msg_email.setWindowTitle("Your Email is not Valid")
            msg_email.setText("The Email Pattern is not True")
            msg_email.setIcon(QMessageBox.Warning)
            msg_email.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    signUp_View = SignUp()
    app.exec_()
