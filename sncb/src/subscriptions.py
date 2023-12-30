def compute_sncb_subscription(
    user_age:int,
    user_working_status: str,
)->int:
    """
    Computes the price of the SCNB subscription of a client based on its personal info.
    
    Rules are the following:
    - default price is 800 euros
    - if student under 24 years old : 50 euros
    - if retired : 100 euros

    Parameters
    ----------
    user_age : int
        the age of the user
    user_working_status : str
        the working status of the user ("retired", "student", "employed", "unemployed")
    Returns
    -------
    int
        the price of the SCNB subscription of a client based on its personal info
    """
    pass