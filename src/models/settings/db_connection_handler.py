import sqlite3
from sqlite3 import Connection

class DbConnectionHandler:
    def __init__(self) -> None:#Constructor method
        self.__connection_string = "storage.db"#Directory to our database
        self.__conn = None
    def connect(self) -> None:#method to connect to the database
        conn=sqlite3.connect(self.__connection_string, check_same_thread=False)
        self.__conn=conn
    def get_connection(self) -> Connection:
        return self.__conn

db_connection_handler=DbConnectionHandler()#Create a connection to the database