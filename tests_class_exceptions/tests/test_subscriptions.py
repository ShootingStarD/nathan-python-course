import pytest

from tests_class_exceptions.src.subscriptions import compute_sncb_subscription
from tests_class_exceptions.src.user import User


def test_student_plan():
    age = 24
    working_status = "student"
    expected_price = 50
    actual_price = compute_sncb_subscription(
        User(age, working_status)
    )
    assert actual_price == expected_price


def test_boomer_plan():
    age = 68
    working_status = "retired"
    expected_price = 100
    actual_price = compute_sncb_subscription(
        User(age, working_status)
    )
    assert actual_price == expected_price


def test_invalid_retired_exception():
    age = 28
    working_status = "retired"
    with pytest.raises(ValueError):
        actual_price = compute_sncb_subscription(
            User(age, working_status)
        )
