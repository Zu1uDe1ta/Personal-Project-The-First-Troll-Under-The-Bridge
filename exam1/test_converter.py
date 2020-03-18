



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
    kilometers = float(input("Enter distance in kilometers:"))
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
    miles = float(input("Enter distance in kilometers:"))
    conv = 0.621371
    kilometers = miles / conv
    print('%0.2f miles is equal to %0.2f miles' % (miles, kilometers))









# class ConverterTest(unittest.TestCase):

    def test_meters_to_feet(self):
        test_cases = [
            (1, 3.28),
            (5, 16.40),
            (10, 32.81),
            (100, 328.08),
            (0.91, 2.99),
        ]

        for meter_in, expected in test_cases:
            with self.subTest(f"{meter_in} -> {expected}"):
                self.assertEqual(expected, converter.meters_to_feet(meter_in))


    def test_feet_to_meters(self):
        test_cases = [
            (1, .30),
            (33, 10.06),
            (125, 38.10)
        ]

        for feet_in, expected in test_cases:
            with self.subTest(f"{feet_in} -> {expected}"):
                self.assertEqual(expected, converter.feet_to_meters(feet_in))

    def test_kilometer_to_miles(self):
        test_cases = [
            (1, 0.62),
            (5, 3.11),
            (10, 6.21),
            (42, 26.1)
        ]

        for kilometer_in, expected in test_cases:
            with self.subTest(f"{kilometer_in} -> {expected}"):
                self.assertEqual(expected, converter.kilometer_to_miles(kilometer_in))

    def test_miles_to_kilometers(self):
        test_cases = [
            (1, 1.61),
            (3, 4.83),
            (26.2, 42.16),
            (55, 88.51),
        ]

        for mile_in, expected in test_cases:
            with self.subTest(f"{mile_in} -> {expected}"):
                self.assertEqual(expected, converter.miles_to_kilometers(mile_in))
