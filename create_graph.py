from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QRadioButton, QPushButton
from PyQt5 import uic
import sys


class CreateGraph(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.loadUi("create_graph.ui", self)

        self.setFixedSize(436, 579)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    createGraph = CreateGraph()
    app.exec_()
