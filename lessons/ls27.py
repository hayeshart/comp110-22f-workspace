from typing import Union

def add(lhs: float = 0.0, rhs: Union[str, float] = 0.0) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result

print(add())
print(add(1.0))
print(add(1.0, 2.0))
print(add(2.0,"1.0"))

print(add(110))
print(add(110.0, "100.0"))