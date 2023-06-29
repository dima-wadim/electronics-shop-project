import pytest
from src.phone import Keyboard


@pytest.fixture()
def kb_name():
    return Keyboard("Dark Project KD87A", 9600, 5)


def test_str(kb_name):
    assert str(kb_name) == "Dark Project KD87A"
    assert str(kb_name.language) == "EN"


def test_repr(kb_name):
    assert repr(kb_name) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test_change_lang(kb_name):
    kb_name.change_lang()
    assert str(kb_name.language) == "RU"
    kb_name.change_lang().change_lang()
    assert str(kb_name.language) == "RU"