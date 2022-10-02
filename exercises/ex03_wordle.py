"""EX03 - Structured Wordle."""

__author__ = "730549088"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search_second: str, single_character: str) -> bool: 
    """Search_second is searching through single_character and iterating through the string to check for a match."""
    assert len(single_character) == 1
    while search_second > '':
        if search_second[0] == single_character:
            return True
        else:
            search_second = search_second[1:]
    return False


def emojified(six_letter_word: str, secret_word: str) -> str: 
    """This function checks the user's six_letter_guess against the secret_word to give them the appopriate box."""
    assert len(six_letter_word) == len(secret_word)
    blank_box: str = ""
    counter: int = 0
    while len(secret_word) > counter:
        if (six_letter_word[counter]) == secret_word[counter]:
            blank_box += GREEN_BOX
        elif contains_char(secret_word, six_letter_word[counter]) is False:  
            blank_box += WHITE_BOX 
        else:
            blank_box += YELLOW_BOX
        counter += 1
    return blank_box


def input_guess(n: int) -> str:
    """This function allows the user to insert a guess for the wordle."""
    prompt: str = input(f"Enter a {n} character word: ")
    while len(prompt) != n: 
        prompt = input(f"That wasn't {n} chars! Try again: ")
    return prompt


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    turn: int = 0
    secret_word: str = "codes"
    correct: bool = False
    while turn < 6 and not correct: 
        turn += 1 
        print(f"=== Turn {turn}/6 ===")
        guessed_word: str = input_guess(len(secret_word))
        print(emojified(guessed_word, secret_word))
        if guessed_word == secret_word: 
            print(f"You won in {turn}/6 turns!")
            correct = True
        elif turn > 5: 
            print("X/6 - Sorry, try again tomorrow! ")