"""EX06 - Choose Your Own Adventure."""


__author__: "730549088"


def main() -> None: 
    global points
    points = 0
    global SPARKLE
    SPARKLE = "\U00002728"
    greet()
    instructions()
    question_1_prompt()
    question_1_response()
    question_2_prompt()
    question_2_response()
    question_3_prompt()
    question_3_response()
    question_4_prompt()
    question_4_response()
    results()
    user_satisfied()
    game_loop()


def greet() -> None:
    print("Hello! Let's find out what Disney Princess you are!")
    print()
    global player
    player = input("First, what is your name? ")
    print()
    print(f'Nice to meet you, {player}! Here are some instructions:')
    print("1. Please input the letter associated with your answer choice.")
    print("2. Your results will be based on the number of points you score.")
    print("3. Have fun while playing!")
    print()
        

def instructions() -> None: 
    understand_instructions: str = input("Do you understand? ")
    if understand_instructions == "Yes":
        print(f"Yay! Let's begin, {player}.")
    elif understand_instructions == "yes": 
        print(f"Yay! Let's begin, {player}.")
    elif understand_instructions == "No": 
        print("I'm sorry about that. Please play again another time then.")
        quit()
    elif understand_instructions == "no": 
        print("I'm sorry about that. Please play again another time then.")
        quit()
    else:
        print("Error: Not an accepted response. Please try again.")
        return instructions()


def question_1_prompt() -> None: 
    print()
    print("First Question:")
    print("What is your favorite color?")
    print("A) Blue")
    print("B) Yellow")
    print("C) Green")
    print("D) Purple")


def question_1_response() -> None: 
    q1_answer: str = input("Answer: ")
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
    q2_answer: str = input("Answer: ")
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
    q3_answer: str = input("Answer: ")
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
    print()
    print(f"{player}, it's the last question!")
    print()
    print("Fourth Question:")
    print("How do people usually describe you?")
    print("A) Energetic")
    print("B) Independent")
    print("C) Hardworking")
    print("D) Quiet")


def question_4_response() -> None: 
    q4_answer: str = input("Answer: ")
    if q4_answer == "A":
        global points
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
        return question_4_response() 


def results() -> None: 
    print()
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
    
    if points <= 5: 
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
    FAIRY_EMOJI: str = "\U0001F9DA"
    CLOCK: str = "\U0001F55B"
    MOON: str = "\U0001F315"
    PUMPKIN: str = "\U0001F383"
    SHOE: str = "\U0001F460"
    BROOM: str = "\U0001F9F9"
    print(SPARKLE, BROOM, FAIRY_EMOJI, PUMPKIN, SHOE, CLOCK, MOON, SPARKLE)


def belle() -> None: 
    BOOKS: str = "\U0001F4DA"
    ROSE: str = "\U0001F339"
    TEAPOT: str = "\U0001FAD6"
    YELLOW_HEART: str = "\U0001F49B"
    CROISSANT: str = "\U0001F950"
    BISON: str = "\U0001F9AC"
    print(SPARKLE, CROISSANT, BOOKS, ROSE, TEAPOT, YELLOW_HEART, BISON, SPARKLE)


def jasmine() -> None:
    GENIE: str = "\U0001F9DE"
    TIGER: str = "\U0001F405"
    STAR: str = "\U0001F320"
    DIAMOND: str = "\U0001F48E"
    CROWN: str = "\U0001F451"
    MAGIC_WAND: str = "\U0001FA84"
    print(SPARKLE, GENIE, MAGIC_WAND, CROWN, STAR, TIGER, DIAMOND, SPARKLE) 


def rapunzel() -> None:
    HAIRCUT: str = "\U0001F487"
    LIZARD: str = "\U0001F98E"
    SHOOTING_STAR: str = "\U0001F320"
    BOUQET: str = "\U0001F490"
    PALLETE: str = "\U0001F3A8"
    CASTLE: str = "\U0001F3F0"
    print(SPARKLE, CASTLE, PALLETE, LIZARD, SHOOTING_STAR, BOUQET, HAIRCUT, SPARKLE)


def user_satisfied() -> None: 
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
    play_again: str = input("Would you like to take the quiz again? ")
    if play_again == "No": 
        print(f"Thanks for playing then! Goodbye for now, {player}.")
        quit()
    elif play_again == "no": 
        print(f"Thanks for playing then! Goodbye for now, {player}.")
        quit()
    elif play_again == "Yes": 
        print(f"Sweet! Let's go!")
        main()
    elif play_again == "yes": 
        print(f"Sweet! Let's go!")
        print()
        main()
    else: 
        print("Error: Not an accepted response.")
        return game_loop()



if __name__ == "__main__": 
    main()