import mock
import pytest
import sqlite3
from .context import main


SAMPLE_REGISTERED_USERNAME: str = "User1"
SAMPLE_REGISTERED_PASWORD: str = "$Aample123"
SAMPLE_UNREGISTERED_USERNAME: str = "User2"
SAMPLE_UNREGISTERED_PASSWORD: str = "$Ample123"
SAMPLE_SHORT_PASSWORD: str = "$Amp1e"
SAMPLE_LONG_PASSWORD: str = "$Amp1e long password"
SAMPLE_NO_UPPER_PASSWORD: str = "$ample123"
SAMPLE_NO_DIGIT_PASSWORD: str = "$Ampleabc"

mock_db = None
test_db = None

def populate_db(db) -> None:
    """Populates a db with a single user"""
    query = "CREATE TABLE IF NOT EXISTS Username(username TEXT, password TEXT)"
    db.cursor().execute(query)
    query = "INSERT INTO Username (username, password) VALUES(?, ?);"
    db.cursor().execute(query, (SAMPLE_REGISTERED_USERNAME, SAMPLE_REGISTERED_PASWORD))
    db.commit()


def setup_module(module) -> None:
    global mock_db
    global test_db
    mock_db = sqlite3.connect(':memory:')
    test_db = sqlite3.connect(':memory:')
    populate_db(mock_db)
    main.conn = test_db
    main.c = test_db.cursor()
    

def teardown_module(module) -> None:
    pass


def test_create_table() -> None:
    main.create_table()
    cursor = test_db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    assert cursor.fetchall() == [('Username',)]


def test_data_entry() -> None:
    pass
    

def test_look_value() -> None:
    pass


def test_check_pw() -> None:
    pass


def test_number_rows() -> None:
    pass


def test_login_attempt(capsys) -> None:
    populate_db(test_db)
    main.login_attempt(SAMPLE_REGISTERED_USERNAME, SAMPLE_REGISTERED_PASWORD)
    output = capsys.readouterr()
    assert output.out == "You have successfully logged in\n"

    main.login_attempt(SAMPLE_UNREGISTERED_USERNAME, SAMPLE_UNREGISTERED_PASSWORD)
    output = capsys.readouterr()
    assert output.out == "Incorrect username/password, please try again\n"


def test_main() -> None:
    pass