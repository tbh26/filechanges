import sqlite3


def init_sqlite(db_path: str):
    """helper to initialize sqlite database"""
    connection = sqlite3.connect(db_path)
    return connection.cursor()
