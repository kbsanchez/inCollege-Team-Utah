import pytest
import sqlite3
from typing import Union
from test.context import main, main_menu
from test.utils import add_user

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
    add_user(test_db)
    main.data_entry(SAMPLE_USERNAME, SAMPLE_PASSWORD, SAMPLE_FIRSTNAME, SAMPLE_LASTNAME, 0)
    cursor: sqlite3.Cursor = test_db.cursor()
    query: str = "SELECT * FROM Username WHERE username = ?;"
    cursor.execute(query, (SAMPLE_USERNAME,))
    assert len(cursor.fetchall()) == 1


def test_look_value(capsys) -> None:
    add_user(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
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
    add_user(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    rows: int = main.number_rows()
    assert rows == 1

    add_user(test_db, SAMPLE_UNREGISTERED_USERNAME, SAMPLE_UNREGISTERED_PASSWORD)
    rows = main.number_rows()
    assert rows == 2


# def test_login_attempt(capsys) -> None:
#     add_user(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
#     main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)
#     output = capsys.readouterr()
#     assert output.out == "You have successfully logged in\n"
#
#     main.login_attempt(SAMPLE_UNREGISTERED_USERNAME, SAMPLE_UNREGISTERED_PASSWORD)
#     output = capsys.readouterr()
#     assert output.out == "Incorrect username/password, please try again\n"


def test_create_new_account_with_max(capsys, monkeypatch) -> None:
    max_users = 10
    monkeypatch.setattr('src.main.number_rows', lambda: max_users)
    main.createnewacc()
    output = capsys.readouterr()
    assert output.out == f"The amount of allowed accounts ({max_users}) has been reached\n"


"""
End of sprint 1 test cases, beginning of sprint 2 cases
"""


def test_find_in_db(capsys) -> None:
    add_user(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD, SAMPLE_FIRSTNAME, SAMPLE_LASTNAME)
    main.find_in_db(SAMPLE_FIRSTNAME, SAMPLE_LASTNAME)
    output = capsys.readouterr()
    assert output.out == "They are a part of the InCollege system\n"

    main.find_in_db(SAMPLE_UNREGISTERED_FIRSTNAME, SAMPLE_UNREGISTERED_LASTNAME)
    output = capsys.readouterr()
    assert output.out == "They are not yet a part of the InCollege system yet\n"
#
#
# def test_video_feature(capsys, monkeypatch) -> None:
#     monkeypatch.setattr('src.main', lambda: 's')
#     main.main()
#     output = capsys.readouterr()
#     assert output.out == "video is now playing"


"""
End of sprint 2 test cases
"""


def test_useful_links_choice(capsys, monkeypatch) -> None:
    called = False
    inputs = iter(['u', 'q'])

    def fake_useful_links():
        nonlocal called
        called = True

    main.input = lambda _: next(inputs)
    main.exit = lambda: ()

    monkeypatch.setattr('src.main.usefulllinks', fake_useful_links)

    main.main()
    assert called
