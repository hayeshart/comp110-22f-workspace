"""EX07 - Dictionary Functions."""


__author__ = "730549088"


def invert(a: dict[str, str]) -> dict[str, str]:
    """ When given a dictionary, this function will invert the keys and values."""
    result: dict[str, str] = {}
    result = dict((a[keys], keys) for keys in a) 
    if len(result) != len(a): 
        raise KeyError("You don't have unique keys!")
    return result


def favorite_color(b: dict[str, str]) -> str: 
    """ This function returns the most common str from a dictionary's values."""
    occurences: dict = {}
    for values in b.values():
        if values in occurences:
            occurences[values] += 1
        else: 
            occurences[values] = 1
    k = list(occurences.keys())
    v = list(occurences.values())
    most_frequent_value = k[v.index(max(v))]
    return most_frequent_value


def count(c: list[str]) -> dict[str, int]: 
    """ This function produces a dictionary that shows how many times a unique value appears in a given list."""
    occurences: dict[str, int] = {}
    for int in c:
        if int in occurences:
            occurences[int] += 1
        else: 
            occurences[int] = 1
    return occurences
 