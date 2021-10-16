import sqlite3
from .context import db_session


def get_mock_db():
    mock_db = sqlite3.connect(':memory:')
    db_session.create_tables(mock_db)

    return mock_db


def add_user(db: sqlite3.Connection, username: str = None, password: str = None,
             firstname: str = None, lastname: str = None) -> None:
    """Add user to Username table"""
    create_user_table(db)
    if username is not None and password is not None:
        query = "INSERT INTO Username (username, password, firstname, lastname) VALUES(?, ?, ?, ?);"
        db.cursor().execute(query, (username, password, firstname, lastname))
    db.commit()


def create_user_table(db: sqlite3.Connection):
    query: str = """CREATE TABLE IF NOT EXISTS Username(
    username TEXT PRIMARY KEY,
    password TEXT,
    firstname TEXT,
    lastname TEXT,
    logedIn NOT NULL CHECK (logedIn IN (0, 1)) DEFAULT 0,
    email BOOLEAN NOT NULL CHECK (email IN (0, 1)) DEFAULT 1,
    sms BOOLEAN NOT NULL CHECK (sms IN (0, 1)) DEFAULT 1,
    marketing BOOLEAN NOT NULL CHECK (marketing IN (0, 1)) DEFAULT 1,
    language TEXT DEFAULT 'english');
    """
    db.cursor().execute(query)
    db.commit()


def add_friend(db: sqlite3.Connection, self_username: str = None,
               requested_username: str = None, request: int = 0):
    create_friend_table(db)
    data = (self_username, requested_username, request)
    if self_username is not None and requested_username is not None:
        query = "INSERT INTO Friends(userOne, userRequested, request) VALUES (?,?,?)"
        db.execute(query, data)
    db.commit()


def create_friend_table(db: sqlite3.Connection):
    query = "CREATE TABLE IF NOT EXISTS Friends(userOne TEXT, userRequested TEXT, request INTEGER)"
    db.execute(query)
    db.commit()


def add_profile(db: sqlite3.Connection, username: str, title: str,
                major: str, university: str, about: str):
    create_profile(db)
    query = "INSERT INTO Profile(username, title, major, universityName, about) VALUES (?, ?, ?, ?, ?)"
    db.execute(query, (username, title, major, university, about))
    db.commit()


def create_profile(db: sqlite3.Connection):
    query = """CREATE TABLE IF NOT EXISTS Profile(
    username TEXT PRIMARY KEY,
    title TEXT, 
    major TEXT,
    universityName,
    about)
    """
    db.execute(query)
    db.commit()


def login_user(db: sqlite3.Connection, username: str):
    query = """UPDATE Username SET logedin = 1 WHERE username = ?"""
    db.execute(query, (username, ))
    db.commit()
