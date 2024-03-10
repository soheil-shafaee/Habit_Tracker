from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QRadioButton, QPushButton
from PyQt5 import uic
import sys
from add_pixel import AddPixel
import psycopg2

# --------- DataBase Section -----------
try:
    conx = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="8VMNKEZlg%",
        database="habit_tracker",

    )

    cur = conx.cursor()
    com_users = """SELECT username, token FROM users"""
    cur.execute(com_users)
    users = cur.fetchall()

except Exception as e:
    print(e)


class CreateGraph(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.loadUi("create_graph.ui", self)

        self.setFixedSize(436, 579)

        self.pixel_page = None

        """Define Our Widgets"""
        self.create_graph_button = self.findChild(QPushButton, "create_graph")
        self.graph_id_create = self.findChild(QLineEdit, "id")
        self.graph_name_create = self.findChild(QLineEdit, "graph_name")
        self.username_graph_create = self.findChild(QLineEdit, "username")
        self.password_graph_create = self.findChild(QLineEdit, "password")
        self.unit_graph_create = self.findChild(QLineEdit, "unit")
        self.green = self.findChild(QRadioButton, "green")
        self.yellow = self.findChild(QRadioButton, "yellow")
        self.red = self.findChild(QRadioButton, "red")
        self.purple = self.findChild(QRadioButton, "purple")
        self.blue = self.findChild(QRadioButton, "blue")
        self.black = self.findChild(QRadioButton, "black")

        self.create_graph_button.clicked.connect(self.graph_created)

        self.username_graph_create.setText(users[0][0])
        self.password_graph_create.setText(users[0][1])

        self.show()

    def graph_created(self):
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

        try:
            cur.execute("""INSERT INTO graph VALUES(%s, %s, %s, %s)""",
                        (graph_id, graph_name, unit, color))

            conx.commit()
        except Exception as ERROR:
            print(ERROR)
            conx.rollback()




            # self.pixel_page = AddPixel()
            # self.pixel_page.show()
            # self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    createGraph = CreateGraph()
    app.exec_()
