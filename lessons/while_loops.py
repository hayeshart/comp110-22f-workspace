"""Loops practice!"""

x: int = 0 
y: int = 3 
z: str = "1" 

while x < y:
    z = z + str(y) + str(x)
    x = x + 1 

print(x)
print(y)
print(z)