def odd_and_even(a: list[int]) -> list[int]: 
    i: int = 0 
    new_list: list[int] = []
    while i < len(a): 
        if a[i] % 2 == 0 and i % 2 == 0: 
            new_list.append(a[i])
        i += 1
    return new_list