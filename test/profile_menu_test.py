from . import main_test
from .context import profile_menu, main
from .utils import populate_db, get_mock_db
from .context import db_session
import pytest

from test import utils

mock_db = None
USERNAME = "Jose"
PASSWORD = "123"


@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch) -> None:
    global mock_db
    mock_db = get_mock_db()

    monkeypatch.setattr('src.profile_menu.db', mock_db)
    monkeypatch.setattr('src.main.conn', mock_db)
    monkeypatch.setattr('src.main.c', mock_db.cursor())

    utils.populate_db(mock_db, USERNAME, PASSWORD)
    main.login(USERNAME)

    yield  # test runs


def create_profile(username, menu):
    menu.username = username
    menu.write_db()
    menu.username = str()


def test_read_db_does_not_load_profile_if_non_existant():
    menu = profile_menu.ProfileMenu()
    menu.read_db()

    assert menu.has_profile == False


def test_read_db_loads_profile():
    menu = profile_menu.ProfileMenu()

    create_profile(USERNAME, menu)

    menu.read_db()

    assert menu.has_profile == True


def test_get_education_text_empty():
    menu = profile_menu.ProfileMenu()

    assert menu.get_education_text() == "None"


def test_get_experience_text_empty():
    menu = profile_menu.ProfileMenu()

    assert menu.get_experience_text() == "None"


def test_write_db():
    TITLE = "Some title"
    menu = profile_menu.ProfileMenu()

    create_profile(USERNAME, menu)
    menu.read_db()

    menu.user_title = TITLE
    menu.write_db()

    query = """
        SELECT title FROM Profile
        WHERE username=?
        """

    cursor = mock_db.cursor()
    cursor.execute(query, (USERNAME, ))
    result = cursor.fetchone()

    assert result[0] == TITLE
