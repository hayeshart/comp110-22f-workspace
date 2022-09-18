"""EX04 - 'list' Utility Functions."""
__author__ =  730549088

def all (numbers: list[int], given_number: int) -> bool:
    counter: int = 0
    checking_variable: bool = True
    while counter < len((numbers)): 
        if numbers[counter] != given_number:
            checking_variable = False
            return checking_variable
        counter += 1
    return checking_variable

def max(input: list[int]) -> int:
    if len(input) == 0: 
        raise ValueError("max() arg is an empty List")
    counter: int = 0
    maximum_value = input[0]
    while counter < len(input): 
        if input[counter] > maximum_value: 
            maximum_value = input[counter]
        counter += 1
    return maximum_value


def is_equal (list_1: list[int], list_2: list[int]) -> bool: 
    counter: int = 0 
    while counter < len(str(list_1)): 
        if list_1 == list_2:
            return True 
        else: 
            return False
    counter += 1 