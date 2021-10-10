import sqlite3
from .context import db_session


def get_mock_db():
    mock_db = sqlite3.connect(':memory:')
    db_session.create_tables(mock_db)

    return mock_db


def populate_db(db: sqlite3.Connection, username: str = None, password: str = None) -> None:
    """Populates a db with a single user"""
    query: str = "CREATE TABLE IF NOT EXISTS Username(username TEXT, password TEXT)"
    db.cursor().execute(query)

    if username is not None and password is not None:
        query = "INSERT INTO Username (username, password) VALUES(?, ?);"
        db.cursor().execute(query, (username, password))
    db.commit()
