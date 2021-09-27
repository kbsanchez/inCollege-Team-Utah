import pytest
import sqlite3
from typing import Union
from test.context import main, main_menu
from test.utils import populate_db

"""
Beginning of tests for sprint #1
"""

SAMPLE_USERNAME: str = "User1"
SAMPLE_PASSWORD: str = "$Aample123"

SAMPLE_FIRSTNAME: str = "John"
SAMPLE_LASTNAME: str = "Smith"
SAMPLE_UNREGISTERED_FIRSTNAME: str = "Joe"
SAMPLE_UNREGISTERED_LASTNAME: str = "Doe"

SAMPLE_UNREGISTERED_USERNAME: str = "User2"
SAMPLE_UNREGISTERED_PASSWORD: str = "$Ample123"
SAMPLE_SHORT_PASSWORD: str = "$Amp1e"
SAMPLE_LONG_PASSWORD: str = "$Amp1e long password"
SAMPLE_NO_UPPER_PASSWORD: str = "$ample123"
SAMPLE_NO_DIGIT_PASSWORD: str = "$Ampleabc"
SAMPLE_NO_ALPHA_PASSWORD: str = "Sample123"

SAMPLE_IN_RANGE_MENU_SELECTION: int = 1
SAMPLE_IN_RANGE_MENU_SELECTION_2: int = 3
SAMPLE_IN_RANGE_MENU_SELECTION_3: int = 4
SAMPLE_OUT_OF_RANGE_MENU_SELECTION: int = 8

mock_db: Union[sqlite3.Connection, None] = None
test_db: Union[sqlite3.Connection, None] = None


@pytest.fixture(autouse=True)
def run_around_tests() -> None:
    # setup
    global mock_db
    global test_db
    mock_db = sqlite3.connect(':memory:')
    test_db = sqlite3.connect(':memory:')
    main.conn = test_db
    main.c = test_db.cursor()

    yield  # test runs

    # teardown


def test_create_table() -> None:
    main.create_table()
    cursor: sqlite3.Cursor = test_db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    assert cursor.fetchall() == [('Username',)]


def test_data_entry() -> None:
    populate_db(test_db)
    main.data_entry(SAMPLE_USERNAME, SAMPLE_PASSWORD, SAMPLE_FIRSTNAME, SAMPLE_LASTNAME)
    cursor: sqlite3.Cursor = test_db.cursor()
    query: str = "SELECT * FROM Username WHERE username = ?;"
    cursor.execute(query, (SAMPLE_USERNAME,))
    assert len(cursor.fetchall()) == 1


def test_look_value(capsys) -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.input = lambda x: SAMPLE_UNREGISTERED_USERNAME  # to mock input
    result = main.look_value(SAMPLE_USERNAME)
    output = capsys.readouterr()
    assert output.out == "Username already exist.\n"
    assert result == SAMPLE_UNREGISTERED_USERNAME


def test_check_pw(capsys) -> None:
    main.check_pw(SAMPLE_PASSWORD)
    output = capsys.readouterr()
    assert output.out == ""

    main.getpass = lambda: SAMPLE_PASSWORD  # to mock getpass

    main.check_pw(SAMPLE_SHORT_PASSWORD)
    output = capsys.readouterr()
    assert output.out == "Password must be at least 8 and no more than 12 characters in length.\n"

    main.check_pw(SAMPLE_LONG_PASSWORD)
    output = capsys.readouterr()
    assert output.out == "Password must be at least 8 and no more than 12 characters in length.\n"

    main.check_pw(SAMPLE_NO_UPPER_PASSWORD)
    output = capsys.readouterr()
    assert output.out == "Password must contain at least one capital letter\n"

    main.check_pw(SAMPLE_NO_DIGIT_PASSWORD)
    output = capsys.readouterr()
    assert output.out == "Password must contain at least one digit\n"

    main.check_pw(SAMPLE_NO_ALPHA_PASSWORD)
    output = capsys.readouterr()
    assert output.out == "Password must contain at least one alphanumeric symbol\n"


def test_number_rows() -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    rows: int = main.number_rows()
    assert rows == 1

    populate_db(test_db, SAMPLE_UNREGISTERED_USERNAME, SAMPLE_UNREGISTERED_PASSWORD)
    rows = main.number_rows()
    assert rows == 2


def test_login_attempt(capsys) -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)
    output = capsys.readouterr()
    assert output.out == "You have successfully logged in\n"

    main.login_attempt(SAMPLE_UNREGISTERED_USERNAME, SAMPLE_UNREGISTERED_PASSWORD)
    output = capsys.readouterr()
    assert output.out == "Incorrect username/password, please try again\n"


# begin tests for get_user_selection and learn_skills_menu

def test_main_menu_selection_1(monkeypatch) -> None:
    # prereq for test case is being logged in
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)

    monkeypatch.setattr('src.main_menu.get_user_selection', lambda: SAMPLE_IN_RANGE_MENU_SELECTION)
    result = main_menu.get_user_action_selection()
    assert result == None


def test_main_menu_selection_3(monkeypatch) -> None:
    # prereq for test case is being logged in
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)

    monkeypatch.setattr('src.main_menu.get_user_selection', lambda: SAMPLE_IN_RANGE_MENU_SELECTION_2)
    result = main_menu.get_user_action_selection()
    assert result == main_menu.learn_skills_menu


def test_main_menu_selection_4(monkeypatch) -> None:
    # prereq for test case is being logged in
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)

    monkeypatch.setattr('src.main_menu.get_user_selection', lambda: SAMPLE_IN_RANGE_MENU_SELECTION_3)
    result = main_menu.get_user_action_selection()
    assert result == main_menu.logout


def test_skills_menu_selection(monkeypatch) -> None:
    # prereq for test case is being logged in
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)
    monkeypatch.setattr('main_menu.get_user_selection', lambda: SAMPLE_IN_RANGE_MENU_SELECTION)
    output = main_menu.learn_skills_menu()

    assert output.out == "Under Construction"


def test_skills_menu_selection_2(monkeypatch) -> None:
    # prereq for test case is being logged in
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)
    monkeypatch.setattr('main_menu.get_user_selection', lambda: SAMPLE_OUT_OF_RANGE_MENU_SELECTION)
    output = main_menu.learn_skills_menu()

    assert output.out == "Invalid selection"


# end tests for get_user_selection and learn_skills_menu

def test_sixth_user_attempt(capsys, monkeypatch) -> None:
    monkeypatch.setattr('src.main', lambda: 'n')
    main.main()
    output = capsys.readouterr()
    assert output.out == "The amount of allowed accounts (5) has been reached"


"""
End of sprint 1 test cases, beginning of sprint 2 cases
"""


def test_find_in_db(capsys) -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD, SAMPLE_FIRSTNAME, SAMPLE_LASTNAME)
    main.find_in_db(SAMPLE_FIRSTNAME, SAMPLE_LASTNAME)
    output = capsys.readouterr()
    assert output.out == "They are a part of the InCollege system"

    main.find_in_db(SAMPLE_UNREGISTERED_FIRSTNAME, SAMPLE_UNREGISTERED_LASTNAME)
    output = capsys.readouterr()
    assert output.out == "They are not yet a part of the InCollege system yet"


def test_video_feature(capsys, monkeypatch) -> None:
    monkeypatch.setattr('src.main', lambda: 's')
    main.main()
    output = capsys.readouterr()
    assert output.out == "video is now playing"


"""
End of sprint 2 test cases
"""


def test_main() -> None:
    pass