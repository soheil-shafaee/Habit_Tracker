from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QRadioButton, QPushButton
from PyQt5 import uic
import sys
from add_pixel import AddPixel

class CreateGraph(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.loadUi("create_graph.ui", self)

        self.setFixedSize(436, 579)

        self.pixel_page = None

        self.create_graph_button = self.findChild(QPushButton, "create_graph")

        self.create_graph_button.clicked.connect(self.graph_created)

        self.show()

    def graph_created(self):
        self.pixel_page = AddPixel()
        self.pixel_page.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    createGraph = CreateGraph()
    app.exec_()
