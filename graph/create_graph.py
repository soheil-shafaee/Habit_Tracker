from PyQt5.QtWidgets import QMainWindow, QLineEdit, QRadioButton, QPushButton, QMessageBox
from PyQt5 import uic
import requests

from .add_pixel import AddPixel
from database.database import session, Graph


class CreateGraph(QMainWindow):
    """
    This class represents the Create Graph window of the application. It handles the creation of a new graph
    by interacting with the Pixela API and storing the graph details in the local database.

    Attributes:
        pixel_page (AddPixel): The next window to open after creating a graph.
        user_owner_id (int): The ID of the user who owns the graph.
        create_graph_button (QPushButton): Button to trigger the graph creation process.
        graph_id_create (QLineEdit): Input field for the graph ID.
        graph_name_create (QLineEdit): Input field for the graph name.
        username_graph_create (QLineEdit): Input field for the username.
        unit_graph_create (QLineEdit): Input field for the graph unit.
        green (QRadioButton): Radio button for selecting green color.
        yellow (QRadioButton): Radio button for selecting yellow color.
        red (QRadioButton): Radio button for selecting red color.
        purple (QRadioButton): Radio button for selecting purple color.
        blue (QRadioButton): Radio button for selecting blue color.
        black (QRadioButton): Radio button for selecting black color.
        username_graph (str): The username for the graph creation.
        password_graph (str): The token for the graph creation.

    Methods:
        graph_created(): Handles the creation of a graph by interacting with the Pixela API and saving the graph details in the local database.
    """
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
        """
        Function For Creating a Graph by interacting with the Pixela API and saving the graph details
        in the local database.
        """
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



