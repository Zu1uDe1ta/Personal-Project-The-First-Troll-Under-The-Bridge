from typing import List, Tuple, Set, TypeVar

N = TypeVar('N', int, float)
C = TypeVar('C', List, Tuple)


def find_lowest_value(list_in: List[N]) -> N:
    """
    Returns the lowest value in a list of numbers.

    :param list_in: A list of numbers (integers and/or floats)
    :return: The lowest number in the list
    """
    return(min(list_in))


def find_highest_value(list_in: List[N]) -> N:
    """
    Returns the highest value in a list of numbers.

    :param list_in: A list of numbers (integers and/or floats)
    :return: The highest number in the list
    """
    return(max(list_in))



def find_value(value_to_find, values: C) -> int:
    """
    This function evaluates whether a value exists within a List or a Set.
    If the value exists, the function returns the index of the value in the collection.
    If the value does not exist, the function returns -1.

    :param value_to_find: A value that may or may not exist within a collection.
    :param values: A List or a Set.
    :return: an integer. Either the index where the value exists or -1
    """
    for i in values:
        if i == value_to_find:
            return values.index(value_to_find)
        if i != value_to_find:
            return -1



def compare_two_numbers(a: N, b: N) -> int:
    """
    Compares two numbers.

    If the numbers are the same, this function will return the number 0.
    If the first number is greater than the second, this function will return the number 1.
    If the second number is greater than the second, this function will return the number -1.

    :param a: The first number.
    :param b: The second number.
    :return: an integer 0, 1, or -1
    """
    if a == b:
        return(0)
    elif a > b:
        return(1)
    elif b > a:
        return(-1)


def compare_two_strings(a: str, b: str) -> int:
    """
    Compares two strings.

    If the strings have the same length, this function will return the number 0.
    If the first string is longer than the second string, this function will return the number 1.
    If the second string is longer than the first string, this function will return the number -1.

    :param a: The first string.
    :param b: The second string.
    :return: an integer 0, 1, or -1
    """
    a = len(a)
    b = len(b)
    if a == b:
        return(0)
    elif a > b:
        return(1)
    elif b > a:
        return(-1)


def find_common(tuple_a: Tuple, tuple_b: Tuple) -> Set:
    """
    Given two tuples, this function returns a set containing items common in both tuples.

    :param tuple_a: The first tuple.
    :param tuple_b: The second tuple.
    :return: A set containing items common on both tuples.
    """
    tpl1_set = set(tuple_a)
    tpl2_set = set(tuple_b)
    commonElement = (tpl1_set & tpl2_set)
    return(commonElement)


def find_duplicates(tuple_in: Tuple) -> List:
    """
    Given a tuple, this function returns a list of the items that contain more than one instance.

    :param tuple_in: A tuple
    :return: a A list containing duplicate items in the tuple_in parameter
    """
    count_map = []
    for i in tuple_in:
        count_map[i] = count_map.get(i, 0) + 1
        print(count_map)

    listOfTuple = [('a', 'e'), ('b', 'x'), ('b', 'x'),
                   ('a', 'e'), ('b', 'x')]




print(result)


tuple_in = [(1, 2), (3, 4), (5, 6)]

# result list initialization
result = []
for t in tuple_in:
    for x in t:
        result.append(x)







print("**** Find the occurence count an element in the Tuple *****")

# Get the count of how many times 34 appears in tuple
count = tupleObj.count(34)

print("Count of 34 in tuple is : ", count)

# Based on occurrence count check if element exists in tuple
if tupleObj.count(34) > 0:
    print("34 Found in Tuple")
else:
    print("34 Not Found in Tuple")


res = [(val, pow(val, 3)) for val in list1]