"""Exercise 02 Wordle One-Shot"""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str =  "\U0001F7E8"
secret_word: str = "python"

six_letter_word: str = input("What is your 6-letter guess? ")
if len(six_letter_word) != 6:
    input("That was not 6 letters! Try again: ")
