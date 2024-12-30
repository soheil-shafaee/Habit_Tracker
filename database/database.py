from sqlalchemy import Column, create_engine, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

"""
This module defines the database models for a habit tracking application using SQLAlchemy. It includes
two main entities: Users and Graph. The database is set up to connect to a PostgreSQL database.

Attributes:
    DATA_BASE_URL (str): The database connection string used to connect to the PostgreSQL database.
    engine (Engine): The SQLAlchemy engine instance used for database interactions.
    Base (declarative_base): The base class for declarative class definitions.

Classes:
    Users: Represents the users of the application, storing their usernames, tokens, and emails.
    Graph: Represents the graphs created by users to track their habits.

Usage:
    This module sets up the database connection and defines the necessary tables. It also creates
    a session to interact with the database.

Example:
    To create a new user:
    ```python
    new_user = Users(username='example_user', token='user_token', email='user@example.com')
    session.add(new_user)
    session.commit()
    ```

    To create a new graph for a user:
    ```python
    new_graph = Graph(owner_id=new_user.id, graph_id='graph1', graph_name='My First Graph', unit='days', color='blue')
    session.add(new_graph)
    session.commit()
    ```
"""

DATA_BASE_URL = "postgresql+psycopg2://postgres:8VMNKEZlg@localhost:5432/habit_tracker"
engine = create_engine(DATA_BASE_URL)

Base = declarative_base()


class Users(Base):
    """Represents a user in the habit tracking application.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        token (str): The authentication token for the user.
        email (str): The email address of the user, must be unique.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    token = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)


class Graph(Base):
    """Represents a graph created by a user for habit tracking.

    Attributes:
        id (int): The unique identifier for the graph.
        owner_id (int): The identifier of the user who owns the graph.
        graph_id (str): The unique ID for the graph.
        graph_name (str): The name of the graph.
        unit (str): The unit of measurement for the graph.
        color (str): The color associated with the graph.
    """
    __tablename__ = "graph"
    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey("users.id"))
    graph_id = Column(String, nullable=False)
    graph_name = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    color = Column(String, nullable=False)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
