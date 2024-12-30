import re
import sys

import requests
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QRadioButton, QMessageBox, QLabel

from graph.create_graph import CreateGraph
from database.database import Users, session
from .token_hashing import hashing_password


# ------- Validate Email Section -------
def validate_email(email):
    """This function make sure email of the users is validated or not"""
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False


# ----------- SignUp Section ----------

class SignUp(QMainWindow):
    """
    This class represent Sing up window of application. It handles create user into database and
    post request for creating user into Api, validate the user email, terms info, visibility of password,

    Attributes:
        signup(QPushButton): Creating new user in database and API.
        hide_show_password(QPushButton): The button to toggle password visibility.
        username_create(QLineEdit): Username that user put for account.
        password_create(QLineEdit): Password that user put for account.
        email_create(QLineEdit): Email that user put for account.
        agree_terms_create(QRadioButton): Check user read the terms of service.
        agree_terms_text(QLabel): The text of terms service.
        graph (CreateGraph): An instance of the CreateGraph class for navigating to the graph section.

    Methods:
        __init__(): Initializes the sign-up window, loads the UI, and sets up the widgets.
        create_new_user(): Creates a new user, saves the user to the database, and sends a POST request to the API.
        """
    def __init__(self):
        super(QMainWindow, self).__init__()

        """Load The UI File"""
        uic.loadUi("create_account.ui", self)
        self.setFixedSize(436, 579)

        """Define Variable For using Class"""
        self.graph = None
        terms_url = "Agree of <a href='https://github.com/a-know/Pixela/wiki/Terms-of-Service'>Terms of Service"

        """Define our widgets"""
        self.signup_button = self.findChild(QPushButton, "signup")
        self.hide_show_password = self.findChild(QPushButton, "hide_show")
        self.username_create = self.findChild(QLineEdit, "username")
        self.password_create = self.findChild(QLineEdit, "password")
        self.email_create = self.findChild(QLineEdit, "email")
        self.agree_terms_create = self.findChild(QRadioButton, "terms")
        self.terms_text = self.findChild(QLabel, "terms_text")

        """Do Action with our widgets"""
        self.signup_button.clicked.connect(self.create_new_user)
        self.hide_show_password.clicked.connect(self.visibility_password)
        self.terms_text.setOpenExternalLinks(True)
        self.terms_text.setText(terms_url)

        """Show The Main Window"""
        self.show()

    def create_new_user(self):
        """
        Creates a new user and saves the user into the database. It also sends a POST request to
        an external API for user creation. The function validates the user input fields, checks if
        the terms of service are agreed upon, and handles any errors that might occur during the process."""
        name = self.username_create.text()
        f_token = self.password_create.text()
        email = self.email_create.text()
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowIcon(QtGui.QIcon("../images/monster.png"))
        if len(name) != 0 and len(f_token) != 0 and len(email) != 0:
            if len(f_token) <= 8:
                msg_box.setWindowTitle("Password ERROR")
                msg_box.setText("Password have to more than 8 characters!")
                msg_box.exec_()
                return
            token = hashing_password(f_token)
            if validate_email(email) and self.agree_terms_create.isChecked():
                try:

                    URL = "https://pixe.la/v1/users"

                    user_json = {
                        "token": token,
                        "username": name,
                        "agreeTermsOfService": "yes",
                        "notMinor": "yes"
                    }

                    response_create = requests.post(url=URL, json=user_json)

                    if response_create.status_code >= 400:
                        msg_box.setWindowTitle("The request contains bad syntax!")
                        msg_box.setText(response_create.text)
                        msg_box.exec_()
                        return
                    new_user = Users(username=name, token=token, email=email)
                    session.add(new_user)
                    session.commit()

                    self.graph = CreateGraph(name, token, new_user.id)
                    self.graph.show()
                    self.close()

                except Exception as error:
                    msg_box.setWindowTitle("Something Went Wrong!")
                    msg_box.setText(f"The Problem is: {error}")
                    msg_box.exec_()
                    session.rollback()

            elif not self.agree_terms_create.isChecked():
                msg_box.setWindowTitle("Terms is not checked")
                msg_box.setText("Please Read The terms of service!!")
                msg_box.exec_()

            else:
                msg_box.setWindowTitle("Your Email is not Valid")
                msg_box.setText("The Email Pattern is not True")
                msg_box.exec_()
        else:
            msg_box.setWindowTitle("Missing Fields")
            msg_box.setText("Please Check your Input, Required Field is Empty!")
            msg_box.exec_()

    def visibility_password(self):
        """
        Toggles the visibility of the password input field. If the password is currently visible,
        it hides it, and if it is currently hidden, it makes it visible."""
        if self.password_create.echoMode() == QLineEdit.Normal:
            self.password_create.setEchoMode(QLineEdit.Password)
        else:
            self.password_create.setEchoMode(QLineEdit.Normal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    signUp_View = SignUp()
    app.exec_()
