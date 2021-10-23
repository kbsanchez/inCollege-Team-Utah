import pytest
from .utils import *
from .context import friends
from typing import Optional

SAMPLE_SELF_USERNAME: str = "self username"
SAMPLE_SELF_FIRSTNAME: str = "self firstname"
SAMPLE_SELF_LASTNAME: str = "self lastname"
SAMPLE_FRIEND_USERNAME: str = "friend username"
SAMPLE_FRIEND_FIRSTNAME: str = "friend firstname"
SAMPLE_FRIEND_LASTNAME: str = "friend lastname"
SAMPLE_PASSWORD: str = "P@ssword12"
SAMPLE_TITLE: str = "Title"
SAMPLE_UNIVERSITY: str = "University"
SAMPLE_MAJOR: str = "Major"
SAMPLE_ABOUT: str = "About"
mock_db: Optional[sqlite3.Connection] = None
cursor: Optional[sqlite3.Cursor] = None


@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch) -> None:
    global mock_db, cursor
    mock_db = get_mock_db()
    cursor = mock_db.cursor()
    add_user(mock_db, SAMPLE_SELF_USERNAME, SAMPLE_PASSWORD,
             SAMPLE_SELF_FIRSTNAME, SAMPLE_SELF_LASTNAME)
    add_user(mock_db, SAMPLE_FRIEND_USERNAME, SAMPLE_PASSWORD,
             SAMPLE_FRIEND_FIRSTNAME, SAMPLE_FRIEND_LASTNAME)
    monkeypatch.setattr('src.friends.c', mock_db.cursor())

    yield

    mock_db.close()


def test_create_friends_table():
    friends.create_friends_table()
    query: str = "SELECT name FROM sqlite_master WHERE type='table' AND name='Friends'"
    cursor.execute(query)
    assert cursor.fetchall()


def test_friends_entry():
    create_friend_table(mock_db)
    friends.friends_entry(SAMPLE_SELF_LASTNAME, SAMPLE_FRIEND_USERNAME, 0)
    query: str = "SELECT * FROM Friends"
    cursor.execute(query)
    assert cursor.fetchall()


def test_search_for_user_by_lastname():
    mock_input = ["1", SAMPLE_FRIEND_LASTNAME]
    friends.input = lambda _: mock_input.pop(0)
    result = friends.search_for_user()
    assert result == SAMPLE_FRIEND_USERNAME


def test_search_for_user_by_university():
    add_profile(mock_db, SAMPLE_FRIEND_USERNAME, SAMPLE_TITLE, SAMPLE_MAJOR, SAMPLE_UNIVERSITY, SAMPLE_ABOUT)
    mock_input = ["2", SAMPLE_UNIVERSITY]
    friends.input = lambda _: mock_input.pop(0)
    result = friends.search_for_user()
    assert result == SAMPLE_FRIEND_USERNAME


def test_search_for_user_by_major():
    add_profile(mock_db, SAMPLE_FRIEND_USERNAME, SAMPLE_TITLE, SAMPLE_MAJOR, SAMPLE_UNIVERSITY, SAMPLE_ABOUT)
    mock_input = ["3", SAMPLE_MAJOR]
    friends.input = lambda _: mock_input.pop(0)
    result = friends.search_for_user()
    assert result == SAMPLE_FRIEND_USERNAME


def test_send_request():
    add_friend(mock_db, SAMPLE_SELF_USERNAME, SAMPLE_FRIEND_USERNAME, 0)
    friends.send_request(SAMPLE_SELF_USERNAME, SAMPLE_FRIEND_USERNAME)
    query = "SELECT request FROM Friends WHERE userOne= ? AND userRequested= ?"
    cursor.execute(query, (SAMPLE_SELF_USERNAME, SAMPLE_FRIEND_USERNAME))
    assert cursor.fetchone()[0] == 1


def test_decline_request():
    add_friend(mock_db, SAMPLE_SELF_USERNAME, SAMPLE_FRIEND_USERNAME, 1)
    friends.decline_request(SAMPLE_SELF_USERNAME, SAMPLE_FRIEND_USERNAME)
    query = "SELECT request FROM Friends WHERE userOne= ? AND userRequested= ?"
    cursor.execute(query, (SAMPLE_SELF_USERNAME, SAMPLE_FRIEND_USERNAME))
    assert cursor.fetchone()[0] == 0


def test_accept_request():
    add_friend(mock_db, SAMPLE_SELF_USERNAME, SAMPLE_FRIEND_USERNAME, 0)
    friends.accept_request(SAMPLE_SELF_USERNAME,SAMPLE_FRIEND_USERNAME)
    query = "SELECT request FROM Friends WHERE userOne= ? AND userRequested= ?"
    cursor.execute(query, (SAMPLE_SELF_USERNAME, SAMPLE_FRIEND_USERNAME))
    assert cursor.fetchone()[0] == 2


def test_read_friend_requests(capsys):
    add_friend(mock_db, SAMPLE_FRIEND_USERNAME, SAMPLE_SELF_USERNAME, 1)
    friends.read_friend_requests(SAMPLE_SELF_USERNAME)
    output = capsys.readouterr()
    assert output.out == f"You have 1 new friend requests from \n{SAMPLE_FRIEND_USERNAME} "


def test_my_friends_list():
    add_friend(mock_db, SAMPLE_SELF_USERNAME, SAMPLE_FRIEND_USERNAME, 2)
    login_user(mock_db, SAMPLE_SELF_USERNAME)
    result = friends.my_friends_list()
    assert result == [SAMPLE_FRIEND_USERNAME]

