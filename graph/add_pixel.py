from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from PyQt5 import uic
from datetime import datetime
import requests
from .link_page import LinkPage


class AddPixel(QMainWindow):
    """
    This class represents the Add Pixel window of the application. It handles the addition of a pixel to a graph
    by interacting with the Pixela API.

    Attributes:
        link_page (LinkPage): The next window to open after adding a pixel.
        add_pixel (QPushButton): Button to trigger the addition of a pixel.
        graph_id_add_pixel (QLineEdit): Input field for the graph ID.
        graph_name_add_pixel (QLineEdit): Input field for the graph name.
        date_add_pixel (QLineEdit): Input field for the date.
        quantity_add_pixel (QLineEdit): Input field for the quantity of the pixel.
        username_graph (str): The username for the graph.
        token_graph (str): The token for the graph.
        graph_id_graph (str): The ID of the graph.
        graph_name_graph (str): The name of the graph.
        datetime_now (str): The current date in the format YYYYMMDD.

    Methods:
        click_add_pixel(): Handles the addition of a pixel by sending data to the Pixela API.
    """
    def __init__(self, username_add_pixel, token_add_pixel, graph_id_add_pixel, graph_name_add_pixel):
        super(QMainWindow, self).__init__()

        uic.loadUi("ui/add_pixel.ui", self)

        self.setFixedSize(436, 579)
        self.link_page = None

        """Define Our Widgets"""
        self.add_pixel = self.findChild(QPushButton, "add_pixel")
        self.graph_id_add_pixel = self.findChild(QLineEdit, "id")
        self.graph_name_add_pixel = self.findChild(QLineEdit, "graph_name")
        self.date_add_pixel = self.findChild(QLineEdit, "date")
        self.quantity_add_pixel = self.findChild(QLineEdit, "quantity")

        """ADD Data To Attribute"""
        self.username_graph = username_add_pixel
        self.token_graph = token_add_pixel
        self.graph_id_graph = graph_id_add_pixel
        self.graph_name_graph = graph_name_add_pixel

        """Today Date"""
        self.datetime_now = datetime.now().strftime("%Y%m%d")

        """ADD Text to our Line Edit"""
        self.graph_id_add_pixel.setText(self.graph_id_graph)
        self.graph_name_add_pixel.setText(self.graph_name_graph)
        self.date_add_pixel.setText(self.datetime_now)

        """To Do Action Our Widgets"""
        self.add_pixel.clicked.connect(self.click_add_pixel)

        """Show The Main Window"""
        self.show()

    def click_add_pixel(self):
        """
        Function to send data to the Pixela API for adding a pixel to the graph.
        """
        quantity = self.quantity_add_pixel.text()
        try:
            URL = f"https://pixe.la/v1/users/{self.username_graph}/graphs/{self.graph_id_graph}"
            HEADERS_PIXEL = {
                "X-USER-TOKEN": self.token_graph
            }

            graph_item = {
                "date": self.datetime_now,
                "quantity": quantity
            }

            response_pixel = requests.post(url=URL, headers=HEADERS_PIXEL, json=graph_item)

            print(response_pixel.text)
            self.link_page = LinkPage(self.username_graph, self.graph_id_graph)
            self.link_page.show()
            self.close()


        except Exception as ER:
            print(ER)
