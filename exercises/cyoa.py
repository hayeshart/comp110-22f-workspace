"""EX06 - Choose Your Own Adventure."""


__author__ = "730549088"

import re


points: int = 0 
SPARKLE: str = "\U00002728"
player: str = ""


def main() -> None: 
    """This is the main function that controls the order in which all of the other functions are run.""" 
    global points
    greet()
    begin()
    question_1_prompt()
    question_1_response()
    question_2_prompt()
    question_2_response()
    question_3_prompt()
    question_3_response()
    question_4_prompt()
    points = question_4_response(points)
    results()
    user_satisfied()
    game_loop()


def greet() -> None:
    """This function starts the program by introducing the topic."""
    """It prompts the user to input their name and prints out the instructions for the quiz."""
    print("Hello! Let's find out what Disney Princess you are!")
    print()
    global player
    player = input("First, what is your name? ")
    print()
    print(f"Nice to meet you, {player}!")
        

def instructions() -> None: 
    """This function asks the user if they understand the instructions provided in the previous function."""
    """If the user doesn't understand, the program is stopped and the user has to restart from the beginning."""
    """If the user does understand, the programa is continued."""
    understand_instructions: str = input("Do you understand? ")
    if understand_instructions == "Yes":
        print(f"Yay! Let's begin, {player}.")
    elif understand_instructions == "yes": 
        print(f"Yay! Let's begin, {player}.")
    elif understand_instructions == "No": 
        print("I'm sorry about that. Here they are again.")
        print()
        print("1. Please input the letter associated with your answer choice.")
        print("2. Your results will be based on the number of points you score.")
        print("3. Have fun while playing!")
        print()
        return instructions()
    elif understand_instructions == "no": 
        print("I'm sorry about that. Here they are again.")
        print()
        print("1. Please input the letter associated with your answer choice.")
        print("2. Your results will be based on the number of points you score.")
        print("3. Have fun while playing!")
        print()
        return instructions()
    else:
        print("Error: Not an accepted response. Please try again.")
        print()
        print("1. Please input the letter associated with your answer choice.")
        print("2. Your results will be based on the number of points you score.")
        print("3. Have fun while playing!")
        print()
        return instructions()


def begin() -> None: 
    print()
    ready_to_start: str = input("Would like to go straight to results, the first question, or see the intstructions? ")
    if ready_to_start == "First question":
        print("Great! Here's the first question.")
    elif ready_to_start == "Question": 
        print("Great! Here's the first question.")
    elif ready_to_start == "first question": 
        print("Great! Here's the first question.")
    elif ready_to_start == "question": 
        print("Great! Here's the first question.")
    elif ready_to_start == "results": 
        points = 0 
        results()
        user_satisfied()
        game_loop()
    elif ready_to_start == "see the instructions": 
        print()
        print("Okay! Here they are...")
        print("1. Please input the letter associated with your answer choice.")
        print("2. Your results will be based on the number of points you score.")
        print("3. Have fun while playing!")
        print()
        instructions()
    elif ready_to_start == "instructions": 
        print()
        print("Okay! Here they are...")
        print("1. Please input the letter associated with your answer choice.")
        print("2. Your results will be based on the number of points you score.")
        print("3. Have fun while playing!")
        print()
        instructions()
    else: 
        print("Error: That is not an accepted response. Please try again.")
        begin()
    


def question_1_prompt() -> None: 
    """This function prints out the prompt for the first question and the possible answer choices."""
    print()
    print("First Question:")
    print("What is your favorite color?")
    print("A) Blue")
    print("B) Yellow")
    print("C) Green")
    print("D) Purple")


def question_1_response() -> None: 
    """This function asks the user for an answer to the first question."""
    """Depending on their input, the value of global points is reassigned."""
    q1_answer: str = input(f"{player}, what is your answer: ")
    if q1_answer == "A":
        global points
        points += 1
        print("Total Points: " + str(points))
    elif q1_answer == "a": 
        points += 1
        print("Total Points: " + str(points))
    elif q1_answer == "B":
        points += 2
        print("Total Points: " + str(points))
    elif q1_answer == "b": 
        points += 2
        print("Total Points: " + str(points))
    elif q1_answer == "C": 
        points += 3 
        print("Total Points: " + str(points))
    elif q1_answer == "c": 
        points += 3 
        print("Total Points: " + str(points))
    elif q1_answer == "D": 
        points += 4
        print("Total Points: " + str((points)))
    elif q1_answer == "d":  
        points += 4
        print("Total Points: " + str((points)))
    else: 
        print("Error: That is not an accepted response. Please try again.")
        return question_1_response()


def question_2_prompt() -> None: 
    """This function prints the second question and the answer choices after a brief comment."""
    print()
    print(f'Three more questions, {player}!')
    print()
    print("Second Question:")
    print("What is your hobby?")
    print("A) Painting")
    print("B) Making Clothes")
    print("C) Stargazing")
    print("D) Reading")


def question_2_response() -> None:
    """This function asks the user to input an answer to question 2."""
    """Depending on their feedback, the value of global points is changed."""
    q2_answer: str = input(f"{player}, what is your answer: ")
    if q2_answer == "A":
        global points
        points += 4
        print("Total Points: " + str(points))
    elif q2_answer == "a": 
        points += 4
        print("Total Points: " + str(points))
    elif q2_answer == "B":
        points += 1
        print("Total Points: " + str(points))
    elif q2_answer == "b": 
        points += 1
        print("Total Points: " + str(points))
    elif q2_answer == "C": 
        points += 3
        print("Total Points: " + str(points))
    elif q2_answer == "c": 
        points += 3 
        print("Total Points: " + str(points))
    elif q2_answer == "D": 
        points += 2
        print("Total Points: " + str((points)))
    elif q2_answer == "d":  
        points += 2
        print("Total Points: " + str((points)))
    else: 
        print("Error: That is not an accepted response. Please try again.")
        return question_2_response()


def question_3_prompt() -> None: 
    """This function prints out the prompt and answer choices for the third question after giving the user some encouragement."""
    print()
    print(f'That was a good choice, {player}!')
    print()
    print("Third Question:")
    print("What is your favorite animal?")
    print("A) Tigers")
    print("B) Chameleons")
    print("C) Bears")
    print("D) Mice")


def question_3_response() -> None:
    """This function prompts the user to input their answer to the third question."""
    """Depending on their answer, the value of global points is changed."""
    q3_answer: str = input(f"{player}, what is your answer: ")
    if q3_answer == "A":
        global points
        points += 3
        print("Total Points: " + str(points))
    elif q3_answer == "a": 
        points += 3
        print("Total Points: " + str(points))
    elif q3_answer == "B":
        points += 4
        print("Total Points: " + str(points))
    elif q3_answer == "b": 
        points += 4
        print("Total Points: " + str(points))
    elif q3_answer == "C": 
        points += 2
        print("Total Points: " + str(points))
    elif q3_answer == "c": 
        points += 2
        print("Total Points: " + str(points))
    elif q3_answer == "D": 
        points += 1
        print("Total Points: " + str((points)))
    elif q3_answer == "d":  
        points += 1
        print("Total Points: " + str((points)))
    else: 
        print("Error: That is not an accepted response. Please try again.")
        return question_3_response()


def question_4_prompt() -> None: 
    """This function prints out the prompt and answer choices for the 4th question."""
    print()
    print(f"{player}, it's the last question!")
    print()
    print("Fourth Question:")
    print("How do people usually describe you?")
    print("A) Energetic")
    print("B) Independent")
    print("C) Hardworking")
    print("D) Quiet")


def question_4_response(points:int) -> int: 
    """This function asks the user what their answer to the fourth question."""
    """It changes the global point value to reflect their answer choice by reassigning the local variable points to the global one."""
    q4_answer: str = input(f"{player}, what is your answer: ")
    if q4_answer == "A":
        points += 4
    elif q4_answer == "a": 
        points += 4
    elif q4_answer == "B":
        points += 3
    elif q4_answer == "b": 
        points += 3
    elif q4_answer == "C": 
        points += 1
    elif q4_answer == "c": 
        points += 1
    elif q4_answer == "D": 
        points += 2
    elif q4_answer == "d":  
        points += 2
    else: 
        print("Error: That is not an accepted response. Please try again.")
        return question_4_response(points) 
    return points

def results() -> None:
    """This function sees how many points the user has and uses this knowledge to determine the user's results."""
    print()
    """This section uses randint to play a little prank on the user. It tells the user that they have a large amount of points before correcting itself."""
    print("Let's see how many total points you have...")
    print()
    import random
    fake_results = str(random.randint(400, 100000))
    print("Wow! " + fake_results + " points!")
    print()
    print("...")
    print()
    print(f"Wait, {player}, that's not right!")
    print()
    print(f"You have {points} points!")
    print()
    print("That means...")
    """Based on the user's points from the quiz, their results are any of the following."""
    if points == 0: 
        print()
        print("I was unable to determine which Disney Princess you are because you did not gain any points.")
        print()
        print(f"Perhaps, {player}, you should take a quiz to see what Disney villian you are...")
        print()
    if 0 < points <= 5:
        print()
        cinderella()
        print(f"{player}, you're Cinderella!")
        cinderella()
        print()
    elif 6 <= points <= 9:
        print() 
        belle()
        print(f"{player}, you're Belle!")
        belle()
        print()
    elif 10 <= points <= 13:
        print()
        jasmine()
        print(f"{player}, you're Jasmine!")
        jasmine()
        print() 
    elif 14 <= points: 
        print()
        rapunzel()
        print(f"{player}, you're Rapunzel!")
        rapunzel()
        print()
        

def cinderella() -> None:
    """This function has all of the emojis used to surround getting the result of Cinderella."""
    FAIRY_EMOJI: str = "\U0001F9DA"
    CLOCK: str = "\U0001F55B"
    MOON: str = "\U0001F315"
    PUMPKIN: str = "\U0001F383"
    SHOE: str = "\U0001F460"
    BROOM: str = "\U0001F9F9"
    print(SPARKLE, BROOM, FAIRY_EMOJI, PUMPKIN, SHOE, CLOCK, MOON, SPARKLE)


def belle() -> None: 
    """This function has all of the emojis used to surround getting the result of Belle."""
    BOOKS: str = "\U0001F4DA"
    ROSE: str = "\U0001F339"
    TEAPOT: str = "\U0001FAD6"
    YELLOW_HEART: str = "\U0001F49B"
    CROISSANT: str = "\U0001F950"
    BISON: str = "\U0001F9AC"
    print(SPARKLE, CROISSANT, BOOKS, ROSE, TEAPOT, YELLOW_HEART, BISON, SPARKLE)


def jasmine() -> None:
    """This function has all of the emojis used to surround getting the result of Jasmine."""
    GENIE: str = "\U0001F9DE"
    TIGER: str = "\U0001F405"
    STAR: str = "\U0001F320"
    DIAMOND: str = "\U0001F48E"
    CROWN: str = "\U0001F451"
    MAGIC_WAND: str = "\U0001FA84"
    print(SPARKLE, GENIE, MAGIC_WAND, CROWN, STAR, TIGER, DIAMOND, SPARKLE) 


def rapunzel() -> None:
    """This function has all of the emojis used to surround getting the result of Rapunzel."""
    HAIRCUT: str = "\U0001F487"
    LIZARD: str = "\U0001F98E"
    SHOOTING_STAR: str = "\U0001F320"
    BOUQET: str = "\U0001F490"
    PALLETE: str = "\U0001F3A8"
    CASTLE: str = "\U0001F3F0"
    print(SPARKLE, CASTLE, PALLETE, LIZARD, SHOOTING_STAR, BOUQET, HAIRCUT, SPARKLE)


def user_satisfied() -> None: 
    """This function sees if the user was statisfied with the quiz."""
    satisfaction: str = input(f"Did you enjoy this quiz, {player}? ")
    if satisfaction == "No": 
        print("Aw, I'm sorry about that.")
    elif satisfaction == "no": 
        print("Aw, I'm sorry about that.")
    elif satisfaction == "Yes": 
        print("Yay, I'm glad!")
    elif satisfaction == "yes": 
        print("Yay, I'm glad!")
    else: 
        print("Error: Not an accepted response.")
        return user_satisfied()
    print()
    

def game_loop() -> None: 
    """This function sees if the user would like to take the quiz again."""
    """If they do, the main function is run again. If not, the user is thanked and the progrma is stopped."""
    global points
    play_again: str = input("Would you like to take the quiz again? ")
    if play_again == "No": 
        print(f"Thanks for playing then! Goodbye for now, {player}.")
        quit()
    elif play_again == "no": 
        print(f"Thanks for playing then! Goodbye for now, {player}.")
        quit()
    elif play_again == "Yes": 
        print("Sweet! Let's go!")
        points = 0
        main()
    elif play_again == "yes": 
        print("Sweet! Let's go!")
        print()
        points = 0
        main()
    else: 
        print("Error: Not an accepted response.")
        return game_loop()



if __name__ == "__main__": 
    main()