from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt5 import uic
import sys
from datetime import datetime
import psycopg2

# --------- DataBase Section -----------
try:
    conx_add_graph = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="8VMNKEZlg%",
        database="habit_tracker",

    )

    cur = conx_add_graph.cursor()
    com_users = """SELECT username, token FROM users"""
    cur.execute(com_users)
    users = cur.fetchall()

    com_graph = """SELECT graph_id, graph_name FROM graph"""
    cur.execute(com_graph)
    graph = cur.fetchall()

except Exception as e:
    print(e)


class AddPixel(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.loadUi("add_pixel.ui", self)

        self.setFixedSize(436, 579)

        """Define Our Widgets"""
        self.add_pixel = self.findChild(QPushButton, "add_pixel")
        self.graph_id_add_pixel = self.findChild(QLineEdit, "id")
        self.graph_name_add_pixel = self.findChild(QLineEdit, "graph_name")
        self.password_add_pixel = self.findChild(QLineEdit, "password")
        self.date_add_pixel = self.findChild(QLineEdit, "date")
        self.quantity_add_pixel = self.findChild(QLineEdit, "quantity")

        self.graph_id_database = graph[0][0]
        self.graph_name_database = graph[0][1]
        self.username_database = users[0][0]
        self.token_database = users[0][1]
        self.datetime_now = datetime.now()
        """ADD Text to our Line Edit"""
        self.graph_id_add_pixel.setText(self.graph_id_database)
        self.graph_name_add_pixel.setText(self.graph_name_database)
        self.password_add_pixel.setText(self.token_database)
        self.date_add_pixel.setText(self.datetime_now.strftime("%Y-%m-%d"))

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    add_pixel = AddPixel()
    app.exec_()
