import os

import psycopg2
from psycopg2.extras import RealDictCursor


class PostgreSQLConnector:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exit_type, value, traceback):
        if self.cursor:
            self.cursor.close()
        self.connection.close()

    def connect(self):
        connection = psycopg2.connect(**self.connection_args())
        connection.set_session(autocommit=True)
        return connection

    @staticmethod
    def connection_args():
        return {
            "host": os.environ.get('DB_HOST'),
            "port": os.environ.get('DB_PORT'),
            "database": os.environ.get('DB_NAME'),
            "user": os.environ.get('DB_USERNAME'),
            "password": os.environ.get('DB_PASSWORD'),
            "cursor_factory": RealDictCursor,
        }
