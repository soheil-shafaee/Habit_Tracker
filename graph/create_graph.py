from PyQt5.QtWidgets import QMainWindow, QLineEdit, QRadioButton, QPushButton, QMessageBox
from PyQt5 import uic
import requests

from add_pixel import AddPixel
from database import session, Graph


class CreateGraph(QMainWindow):
    def __init__(self, username_signup, token_signup, user_id):
        super(QMainWindow, self).__init__()

        """Load The UI File"""
        uic.loadUi("create_graph.ui", self)
        self.setFixedSize(436, 579)

        """Define Variable For using Class"""
        self.pixel_page = None
        self.user_owner_id = user_id

        """Define Our Widgets"""
        self.create_graph_button = self.findChild(QPushButton, "create_graph")
        self.graph_id_create = self.findChild(QLineEdit, "id")
        self.graph_name_create = self.findChild(QLineEdit, "graph_name")
        self.username_graph_create = self.findChild(QLineEdit, "username")
        self.unit_graph_create = self.findChild(QLineEdit, "unit")
        self.green = self.findChild(QRadioButton, "green")
        self.yellow = self.findChild(QRadioButton, "yellow")
        self.red = self.findChild(QRadioButton, "red")
        self.purple = self.findChild(QRadioButton, "purple")
        self.blue = self.findChild(QRadioButton, "blue")
        self.black = self.findChild(QRadioButton, "black")

        """Do Action with our widgets"""
        self.create_graph_button.clicked.connect(self.graph_created)

        """ADD Data To Attribute"""
        self.username_graph = username_signup
        self.password_graph = token_signup

        self.username_graph_create.setText(self.username_graph)

        """Show The Main Window"""
        self.show()

    def graph_created(self):
        """Function For Create Graph"""
        if self.green.isChecked():
            color = "shibafu"
        elif self.yellow.isChecked():
            color = "ichou"
        elif self.red.isChecked():
            color = "momiji"
        elif self.purple.isChecked():
            color = "ajisai"
        elif self.blue.isChecked():
            color = "sora"
        elif self.black.isChecked():
            color = "kuro"

        graph_id = self.graph_id_create.text()
        graph_name = self.graph_name_create.text()
        unit = self.unit_graph_create.text()
        owner_id = self.user_owner_id
        data_insert = (owner_id, graph_id, graph_name, unit, color)


        URL_CREATE_GRAPH = f"https://pixe.la/v1/users/{self.username_graph}/graphs"
        HEADERS = {
            "X-USER-TOKEN": self.password_graph
        }
        graphs_details = {
            "id": graph_id,
            "name": graph_name,
            "unit": unit,
            "type": "int",
            "color": color
        }

        response_create_graph = requests.post(url=URL_CREATE_GRAPH, json=graphs_details, headers=HEADERS)
        error_box = QMessageBox()
        error_response = response_create_graph.text
        if response_create_graph.status_code >= 400:
            error_box.setWindowTitle("The request contains bad syntax")
            error_box.setText(error_response)
            error_box.setIcon(QMessageBox.Warning)
            error_box.exec_()
            return


        new_graph = Graph(owner_id=owner_id, graph_id=graph_id, graph_name=graph_name, unit=unit, color=color)
        session.add(new_graph)
        session.commit()

        self.pixel_page = AddPixel(self.username_graph, self.password_graph, graph_id, graph_name)
        self.pixel_page.show()
        self.close()



