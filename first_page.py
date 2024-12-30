from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
from sys import argv
from second_page import SecondPage


class FirstPage(QMainWindow):
    """Display Wellcome page for users"""
    def __init__(self):
        """Show page with one button"""
        super(QMainWindow, self).__init__()

        """Load The UI File"""
        uic.loadUi("first_page.ui", self)
        self.setFixedSize(436, 579)

        """Define Variable For using Class"""
        self.second_page = None

        """Define our Widgets"""
        self.start = self.findChild(QPushButton, "start_button")

        """Do Action with our widgets"""
        self.start.clicked.connect(self.get_start)

        """Show The Main Window"""
        self.show()

    def get_start(self):
        """Function For going to Second page"""
        self.second_page = SecondPage()
        self.second_page.show()
        self.close()


app = QApplication(argv)
UI = FirstPage()
app.exec_()
