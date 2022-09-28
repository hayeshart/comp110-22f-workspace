"""EX05 - 'list' Utility Functions - implement fuctions."""

__author__ = "730549088"


def only_evens(list_1: list[int]) -> list[int]:
    #This function takes a list of intergers and returns only the even numbers from the list
    only_even_list: list = [] 
    counter: int = 0 
    while counter < len(list_1): 
        #When the number is divided by 2, the remainder should be 0 if it is an even number
        if (list_1[counter] % 2) == 0: 
            only_even_list.append(list_1[counter])
        counter += 1
    return only_even_list


def concat(list_2: list[int], list_3: list[int]) -> list[int]:
    #This function takes two lists and adds the second list after the first list to create a singular list 
    conjoined_list: list = []
    conjoined_list = list_2 + list_3
    return conjoined_list


def sub(list_4: list[int], start: int, end: int) -> list[int]: 
    #This function takes a list and returns the values between specific start and end indexs - 1
    n: int = start
    subset_list: list = [] 
    while (start <= n <= (end - 1)): 
        subset_list.append(list_4[n])
        n += 1 
    return subset_list
