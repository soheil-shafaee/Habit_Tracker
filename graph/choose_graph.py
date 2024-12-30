from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox, QVBoxLayout,    QWidget
from PyQt5 import uic
from .add_pixel import AddPixel
from .create_graph import CreateGraph
from database.database import session, Graph, Users


class ChooseGraph(QMainWindow):
    """
    This class represents the Choose Graph window of the application. It allows users to select an existing graph
    or create a new one, and facilitates the addition of pixels to the selected graph.

    Attributes:
        pixel (AddPixel): The instance of the AddPixel window for adding pixels to a graph.
        graph (CreateGraph): The instance of the CreateGraph window for creating a new graph.
        graph_name_label (QLabel): Label for displaying the names of the user's graphs.
        user (Users): The current user instance fetched from the database.

    Methods:
        display_label(graph_list): Displays the list of graphs in the UI.
        new_graph(): Opens the CreateGraph window for creating a new graph.
        add_pixels(): Opens the AddPixel window for adding pixels to the selected graph.
    """
    def __init__(self, current_user_id):
        super(QMainWindow, self).__init__()
        uic.loadUi("choose_graph.ui", self)
        self.setFixedSize(436, 579)
        self.pixel = None
        self.graph = None
        self.graph_name_label = None
        self.user = session.query(Users).filter(Users.id == current_user_id).first()



        """ Define our widgets"""
        self.add_pixel_button = self.findChild(QPushButton, "add_pixel")
        self.create_graph_button = self.findChild(QPushButton, "create_graph")
        self.graph_container_1 = self.findChild(QWidget, "widget_main")
        self.graph_name_choose = self.findChild(QLineEdit, "graph_name_line")

        """ Add Layout to our widget"""
        self.layout_1 = QVBoxLayout(self.graph_container_1)
        self.graph_container_1.setLayout(self.layout_1)

        """ Find Graph into the database by owner id"""
        graphs = list(session.query(Graph.graph_name).filter(Graph.owner_id == current_user_id).all())
        graphs_list = [graph_info[0] for graph_info in graphs]
        no_graph = QMessageBox()
        if len(graphs_list) == 0:
            no_graph.setWindowTitle("No Graph!")
            no_graph.setText("There is no graph. Please create New Graph")
            no_graph.setIcon(QMessageBox.Warning)
            self.add_pixel_button.setDisabled(True)
            no_graph.exec_()
        else:
            self.no_graph.hide()
            self.add_pixel_button.setDisabled(False)
            self.display_label(graphs_list)
        self.create_graph_button.clicked.connect(self.new_graph)
        self.add_pixel_button.clicked.connect(self.add_pixels)
        self.show()

    def display_label(self, graph_list):
        """
        Displays the names of the user's graphs as labels in the UI.

        Args:
            graph_list (list): A list of graph names to display.
        """
        n = 0
        for graph in graph_list:
            n += 1
            self.graph_name_label = QLabel(f"{n}. "+graph)
            self.graph_name_label.setStyleSheet("""background-color: none;
            color: rgb(255, 255, 255);font:bold 15px Comic Sans MS; border:none""")
            self.layout_1.addWidget(self.graph_name_label)


    def new_graph(self):
        """
        Opens the CreateGraph window for creating a new graph.
        """
        self.graph = CreateGraph(self.user.username, self.user.token, self.user.id)
        self.graph.show()
        self.close()

    def add_pixels(self):
        """
        Opens the AddPixel window for adding pixels to the selected graph.
        """
        graph = session.query(Graph).filter(self.graph_name_choose.text() == Graph.graph_name).first()
        self.pixel = AddPixel(self.user.username, self.user.token, graph.graph_id, graph.graph_name)
        self.pixel.show()
        self.close()
