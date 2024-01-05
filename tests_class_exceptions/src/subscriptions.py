from tests_class_exceptions.src.user import User


def compute_sncb_subscription(
        user: User,
) -> int:
    """
    Computes the price of the SCNB subscription of a client based on its personal info.
    
    Rules are the following:
    - default price is 800 euros
    - if student under 24 years old : 50 euros
    - if retired : 100 euros

    Parameters
    ----------
    user : User
        The client who will compute its info
    Returns
    -------
    int
        the price of the SCNB subscription of a client based on its personal info
    Raises
    ------
        if age < 62 and working status is retired
    """
    if user.age < 62 and user.working_status == "retired":
        raise ValueError("mytho")
    if user.age <= 24 and user.working_status == "student":
        return 50
    elif user.working_status == "retired":
        return 100
    else:
        return 800
