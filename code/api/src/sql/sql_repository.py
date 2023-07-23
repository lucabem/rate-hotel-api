

from src.connector.psql_connector import PostgreSQLConnector
import datetime

class SQLRepository:
    def __init__(self, database, table) -> None:
        self.database = database
        self.table    = table

    @staticmethod
    def execute_select(sql):
        with PostgreSQLConnector() as connector:
            connector.cursor.execute(sql)
            return connector.cursor.fetchall()
        



