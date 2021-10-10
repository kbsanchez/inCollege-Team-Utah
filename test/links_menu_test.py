import pytest
from .context import links_menu


def test_CopyrightNoticeMenu() -> None:
    menu = links_menu.CopyrightNoticeMenu()
    assert menu.title == "Copyright Notice"
    assert menu.subtitle == "This is a copyright notice"


def test_AboutMenu() -> None:
    menu = links_menu.AboutMenu()
    assert menu.title == "About"
    assert menu.subtitle == "This is the about section"


def test_AccessibilityMenu() -> None:
    menu = links_menu.AccessibilityMenu()

    assert menu.title == "Accessibility"
    assert menu.subtitle == "This is the accessibility menu"


def test_UserAgreementMenu() -> None:
    menu = links_menu.UserAgreementMenu()
    assert menu.title == "User Agreement"
    assert menu.subtitle == "This is the user agreement menu"


def test_PrivacyPolicyMenu() -> None:
    menu = links_menu.PrivacyPolicyMenu()
    assert menu.title == "Privacy Policy"
    assert menu.subtitle == "This is the privacy policy"


def test_CopyrightPolicyMenu() -> None:
    menu = links_menu.CopyrightPolicyMenu()
    assert menu.title == "Copyright Policy"
    assert menu.subtitle == "This is our copyright policy"


def test_CookiePolicyMenu() -> None:
    menu = links_menu.CookiePolicyMenu()
    assert menu.title == "Cookie Policy"
    assert menu.subtitle == "This is our cookie policy"


def test_BrandPolicyMenu() -> None:
    menu = links_menu.BrandPolicyMenu()
    assert menu.title == "Brand Policy"
    assert menu.subtitle == "This is our brand policy"
