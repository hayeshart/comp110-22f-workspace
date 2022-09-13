WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001f7e8"

print(GREEN_BOX)
print(WHITE_BOX)
print(YELLOW_BOX)

blank_box: str = ""

blank_box += GREEN_BOX 
YELLOW_BOX += blank_box
print(blank_box)
