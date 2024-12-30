from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from PyQt5 import uic
from datetime import datetime
import requests
from link_page import LinkPage


class AddPixel(QMainWindow):
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
        """Send Data To our Graph"""
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
