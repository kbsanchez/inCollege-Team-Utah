import os
import sqlite3
from typing import Optional
from pathlib import Path

# constants
DB_PATH: str = "Username.db"
DB_SETUP_PATH: str = "setup.sql"

# globals
db: Optional[sqlite3.Connection] = None


def db_init(clean: bool = False) -> sqlite3.Connection:
    """
    create a database and initialize tables
    :param clean: if true delete any existing database
    :return: connection to the database
    """
    global db
    if clean and os.path.isfile(Path(DB_PATH)):
        os.remove(DB_PATH)

    # create database
    db = sqlite3.connect(DB_PATH)
    create_tables(db)

    return db


def create_tables(db):
    cursor = db.cursor()

    # Initialize database with setup file
    with open(Path(DB_SETUP_PATH).absolute(), 'r') as file:
        setup_queries = file.read()
    cursor.executescript(setup_queries)

    db.commit()


db_init()
