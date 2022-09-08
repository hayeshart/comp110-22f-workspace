"""Exercise 02 Wordle One-Shot."""

__author__ = "730549088"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word: str = "python"
six_letter_word: str = input("What is your 6-letter guess? ")
counter: int = 0
blank_box: str = ""

while len(six_letter_word) != 6:
    six_letter_word = input("That was not 6 letters! Try again: ") 

while len(secret_word) > counter:
    if (six_letter_word[counter] == secret_word[counter]):
        blank_box += GREEN_BOX
    else: 
        var_bool: bool = False
        second_counter: int = 0
        while var_bool is False and len(secret_word) > second_counter:
            if six_letter_word[counter] == secret_word[second_counter]:
                var_bool = True
            else:
                second_counter += 1
        if var_bool is True:
            blank_box += YELLOW_BOX
        else:
            blank_box += WHITE_BOX
    counter += 1

print(blank_box)

if (six_letter_word == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")