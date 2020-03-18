def meters_to_feet(meters: float) -> float:
    """
    This function takes a float representing a measurement in meters
    and returns the corresponding value converted to feet.
    The result is rounded to 2 decimal places.

    :param meters: A float representing a measurement in meters.
    :return: A float representing the input measurement converted to feet.
    """
    meters = float(input("Enter height in meters:"))
    feet = meters // .3048
    print('%0.2f meters is equal to %0.2f feet' % (meters, feet))


def feet_to_meters(feet: float) -> float:
    """
    This function takes a float representing a measurement in feet
    and returns the corresponding value converted to meters.
    The result is rounded to 2 decimal places.

    :param feet: A float representing a measurement in feet.
    :return: A float representing the input measurement converted to meters.
    """
    feet = float(input("Enter height in feet:"))
    meters = feet * 0.3048
    print('%0.2f feet is equal to %0.2f meters' % (feet, meters))


def kilometer_to_miles(kilometers: float) -> float:
    """
    This function takes a float representing a measurement in kilometers
    and returns the corresponding value converted to miles.
    The result is rounded to 2 decimal places.

    :param kilometers: A float representing a measurement in kilometers.
    :return: A float representing the input measurement converted to miles.
    """
    kilometers = float(input("Enter height in kilometers:"))
    conv = 0.621371
    miles = kilometers * conv
    print('%0.3f kilometers is equal to %0.2f miles' % (kilometers, miles))



def miles_to_kilometers(miles: float) -> float:
    """
    This function takes a float representing a measurement in miles
    and returns the corresponding value converted to kilometers.
    The result is rounded to 2 decimal places.

    :param miles: A float representing a measurement in miles.
    :return: A float representing the input measurement converted to kilometers.
    """
    pass  # implement me


