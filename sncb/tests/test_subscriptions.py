from sncb.src.subscriptions import compute_sncb_subscription
def test_student_plan():
    age = 24
    working_status = "student"
    expected_price = 50
    actual_price = compute_sncb_subscription(
        user_age=age,
        user_working_status=working_status
    )
    assert actual_price == expected_price