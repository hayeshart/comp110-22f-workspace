"""EX05 - 'list' Utility Functions - test functions."""


__author__ = "730549088"


from exercises.ex05.utils import only_evens, sub, concat


"""Tests for the only_evens function."""


def test_only_evens_no_evens() -> None: 
    """This test gives the only_evens function a list of integers and tests to see if it returns only the even number from the list."""
    """There are no even numbers in this list, so it should return an empty list."""
    xs: list[int] = list([1, 5, 3])
    assert only_evens(xs) == []


def test_only_evens_all_evens() -> None: 
    """This test gives the only_evens function a list of integers and tests to see if it returns only the even number from the list (all the numbers in this case)."""
    xs: list[int] = list([4, 4, 4])
    assert only_evens(xs) == [4, 4, 4]


def test_only_evens_empty() -> None: 
    """This test is looking to see if only_evens is given an empty list, it returns an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_use_case() -> None: 
    """This test gives the only_evens function a list of integers and tests to see if it returns only the even number from the list (2 in this case)."""
    xs: list[int] = list([1, 2, 3])
    assert only_evens(xs) == [2]


def test_only_evens_negative_ints() -> None: 
    """This test gives the only_evens function a list of intergers that includes negatives and tests to see if it only returns the even numbers (2, -8, 6, -2 in this case)."""
    xs: list[int] = [9, -1, 2, 7, -8, 79, 6, 45, -2]
    assert only_evens(xs) == [2, -8, 6, -2]


"""Tests for the concat function."""


def test_concat_empty_list_2() -> None: 
    """This test sees if the concat function returns a list with just the numbers in the second list when the first list is empty."""
    xs: list[int] = list([])
    xm: list[int] = list([9, 8, 7, 34, 765])
    assert concat(xs, xm) == [9, 8, 7, 34, 765]


def test_concat_use_case() -> None: 
    """This test sees if the concat function correctly adds the numbers in list xm after the numbers in list xs in a new list."""
    xs: list[int] = list([8, 6, 43, 65, 89, 12, 5, 7])
    xm: list[int] = list([98, 76, 9, 7, 4, 2, 1])
    assert concat(xs, xm) == [8, 6, 43, 65, 89, 12, 5, 7, 98, 76, 9, 7, 4, 2, 1]


def test_concat_neg_ints() -> None: 
    """This test examines if concat correctly performs when given lists with negative intergers."""
    xs: list[int] = list([-9, -8, 7, 5, 8, -4, 2, -3, 1])
    xm: list[int] = list([7, 6, -5, 4, -2, -3])
    assert concat(xs, xm) == [-9, -8, 7, 5, 8, -4, 2, -3, 1, 7, 6, -5, 4, -2, -3]


def test_concat_empty_list_3() -> None:
    """This test sees if the concat function returns a list with just the numbers in the first list when the second list is empty."""
    xs: list[int] = list([3, 4, 2, 2, 12, 98, 54])
    xm: list[int] = list([])
    assert concat(xs, xm) == [3, 4, 2, 2, 12, 98, 54]


def test_concat_use_case_2() -> None:
    """This test sees if the concat function correctly adds the numbers in list xm after the numbers in list xs in a new list."""
    xs: list[int] = list([405, 989, 984, 745, 879])
    xm: list[int] = list([321, 876, 922, 625, 980])
    assert concat(xs, xm) == [405, 989, 984, 745, 879, 321, 876, 922, 625, 980]


"""Tests for the sub function."""


def test_sub_empty() -> None: 
    """This test sees if sub is given a start is greater than len and len = 0 if it will return an empty list."""
    xs: list[int] = list([])
    start: int = 1
    end: int = 3
    assert sub(xs, start, end) == []


def test_sub_neg_start() -> None: 
    """This test examines if sub is given a neg int as a start index if it will start from the beginning of the list."""
    xs: list[int] = list([50, 60, 70, 80])
    start: int = -1
    end: int = 3
    assert sub(xs, start, end) == [50, 60, 70]


def test_sub_greater_end() -> None: 
    """This test exmaines if sub is given an end int that is greater than the len of the list if it will end with the last int in the list.""" 
    xs: list[int] = list([7, 2, 9, 1])
    start: int = 1
    end: int = 89
    assert sub(xs, start, end) == [2, 9, 1]


def test_sub_use_case_1() -> None: 
    """This test examines if the sub function correctly gives a list on int between a specified start index and the end index - 1."""
    xs: list[int] = list([10, 20, 30, 40])
    start: int = 1 
    end: int = 3 
    assert sub(xs, start, end) == [20, 30]


def test_sub_use_case_2() -> None: 
    """This test examines if the sub function correctly gives a list on int between a specified start index and the end index - 1."""
    xs: list[int] = list([8, 9, 2, 9, 29, 80])
    start: int = 2 
    end: int = 4 
    assert sub(xs, start, end) == [2, 9]