from src.main import main
from .context import main_menu
import pytest


def assert_invalid_selection(selection, capsys):
    main_menu.input = lambda _: selection

    result = main_menu.get_user_action_selection()
    output = capsys.readouterr()

    assert result == None
    assert output.out == "Invalid selection\n"


def test_main_menu_selection_fails_if_value_too_high(capsys):
    selection = len(main_menu.optionsAndActions) + 1
    assert_invalid_selection(selection, capsys)


def test_main_menu_selection_fails_if_value_too_low(capsys):
    selection = 0
    assert_invalid_selection(selection, capsys)


def test_main_menu_selection_under_construction(capsys):
    selection = 1
    main_menu.input = lambda _: selection
    main_menu.optionsAndActions[selection] = (None, None)

    result = main_menu.get_user_action_selection()
    output = capsys.readouterr()

    assert result == None
    assert output.out == "Under Construction\n"


def test_main_menu_selection_action():
    selection = 1
    def action(): return None
    main_menu.input = lambda _: selection
    main_menu.optionsAndActions[selection - 1] = (None, action)

    result = main_menu.get_user_action_selection()

    assert result == action
