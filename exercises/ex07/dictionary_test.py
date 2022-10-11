"""EX07 - Dictionary Functions Tests."""


__author__ = "730549088"


from exercises.ex07.dictionary import favorite_color, invert, count


def test_invert_use_case_1() -> None: 
    """This test checks to see when the function is given a large dictionary it correctly inverts its keys and values."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use_case_2() -> None: 
    """This test also checks to see when the function is given a small dictionary it correctly inverts its keys and values."""
    xs: dict[str, str] = {'apple': 'cat'}
    assert invert(xs) == {'cat': 'apple'}


def test_invert_edge_case() -> None: 
    """This tests checks if invert will return an empty dict when giving an empty dict."""
    xs: dict[str, str] = {'': ''}
    assert invert(xs) == {'': ''}


def test_invert_use_case_3() -> None: 
    """This tests checks if invert will correctly invert when giving a dict with one key and value pair being an empty dict."""
    xs: dict[str, str] = {'': '', 'Piano': 'Awesome', 'Guitar': 'Cool', 'Coding': 'Bad'}
    assert invert(xs) == {'': '', 'Awesome': 'Piano', 'Cool': 'Guitar', 'Bad': 'Coding'}


def test_favorite_color_use_case_1() -> None: 
    """This test checks to see when the function is given a large dictionary it returns the color that appears most frequently."""
    xs: dict[str, str] = {'Panda': 'Orange', 'Pig': 'Pink', 'Horse': 'Yellow', 'Flamingo': 'Pink', 'Rabbit': 'Pink', 'Hippo': 'Yellow', 'Bee': 'Pink'}
    assert favorite_color(xs) == 'Pink'


def test_favorite_color_use_case_2() -> None:  
    """This test checks to see when the function is given a small dictionary it returns the color that appears most frequently."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == 'blue'


def test_favorite_color_edge_case_1() -> None: 
    """This test sees if the given dict contains a key and values that is an empty string, it will still return the color that appears most frequently."""
    xs: dict[str, str] = {"Marc": "yellow", "": "", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_count_use_case_1() -> None: 
    """This test sees if the function correctly counts the frequency of values of a small dict."""
    xs: list[str] = ["Marc", "yellow", "Ezri", "blue", "blue"]
    assert count(xs) == {"Marc": 1, "yellow": 1, "Ezri": 1, "blue": 2}


def test_count_use_case_2() -> None: 
    """This test sees if the function correctly counts the frequency of values of a large dict."""
    xs: list[str] = ['Panda', 'Hippo', 'Panda', 'Flamingo', 'Panda', 'Panda', 'Flamingo', 'Snake']
    assert count(xs) == {'Panda': 4, 'Hippo': 1, 'Flamingo': 2, 'Snake': 1}


def test_count_edge_case() -> None: 
    """This test sees if the function correctly counts the frequency of values when the list contains an empty string."""
    xs: list[str] = ["", "Ballon", "Bat", "Billygoat", "Boat", "Billygoat", "Boat", "Billygoat"]
    assert count(xs) == {"": 1, "Ballon": 1, "Bat": 1, "Billygoat": 3, "Boat": 2}