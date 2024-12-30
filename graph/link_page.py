from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5 import uic



class LinkPage(QMainWindow):
    """
    This class represents the Link Page window of the application. It displays a link to the user's graph
    that can be accessed via a web browser.

    Attributes:
        link (QLineEdit): A line edit widget that displays the URL for accessing the graph.

    Methods:
        __init__(username_link, graph_id_link): Initializes the LinkPage instance and sets up the UI.
    """
    def __init__(self, username_link, graph_id_link):
        super(QMainWindow, self).__init__()

        """Load The UI File"""
        uic.loadUi("link_page.ui", self)
        self.setFixedSize(436, 579)

        """Define our Widgets"""
        self.link = self.findChild(QLineEdit, "link")

        """Do Action Widgets"""
        self.link.setText(f"https://pixe.la/v1/users/{username_link}/graphs/{graph_id_link}.html")

        """Show The Main Window"""
        self.show()
