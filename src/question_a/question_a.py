def get_miles_per_hour(kilometers, minutes):
    """
    Converts kilometers and minutes to miles per hour.
    Returns 'Invalid arguments' if kilometers or minutes are negative.
    """
    if kilometers < 0 or minutes <= 0:
        return 'Invalid arguments'

    miles = kilometers * 0.621371
    hours = minutes / 60
    mph = miles / hours
    return mph
