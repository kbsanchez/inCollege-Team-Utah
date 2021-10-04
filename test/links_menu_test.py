import pytest
import sqlite3
from typing import Union
from test.context import main, main_menu
from test.utils import populate_db

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

def test_CopyrightNoticeMenu(capsys) -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)

    selection = CopyrightNoticeMenu().run
    assert = "This is a copyright notice"


def test_AboutMenu(capsys) -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)

    selection = AboutMenu().run
    assert = "This is the about section"

def test_AccessibilityMenu(capsys) -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)

    selection = AccessibilityMenu().run
    assert = "This is the accessibility menu"

def test_UserAgreementMenu(capsys) -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)

    selection = UserAgreementMenu().run
    assert = "This is the user agreement menu"

def test_PrivacyPolicyMenyu(capsys) -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)

    selection = PrivacyPolicyMenu().run
    assert = "This is the privacy policy"

def test_CookiePolicyMenyu(capsys) -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)

    selection = CookiePolicyMenu().run
    assert = "This is our cookie policy"

def test_CopyrightPolicyMenyu(capsys) -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)

    selection = CopyrightPolicyMenu().run
    assert = "This is our copyright policy"

def test_BrandPolicyMenyu(capsys) -> None:
    populate_db(test_db, SAMPLE_USERNAME, SAMPLE_PASSWORD)
    main.login_attempt(SAMPLE_USERNAME, SAMPLE_PASSWORD)

    selection = BrandPolicyMenu().run
    assert = "This is our brand policy"