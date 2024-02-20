import pytest

from tests_class_exceptions.src.user import User

def test_user_creation():
    loic = User(24, "employed")
    assert loic.age == 24
    assert loic.working_status == "employed"

def test_user_retired_invalid_age():
    with pytest.raises(ValueError):
        menteur = User(25, "retired")
