def convert_to_celsius(fahrenheit):
    """ (number) -> float

    Return the number of Celsius degress equivalent to fahrenheit degress.

    >>> convert_to_celsius(75)
    23.888888888889
    """

    return (fahrenheit - 32.0) * 5.0 / 9.0
