#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import art
from replit import clear


def number_picker():
    return random.randint(1,101)

def number_checker(x,y):
    if x > y:
        return "Too high."
    elif x < y:
        return "Too low."
    else:
        return "You got it right!"


def number_guesser():
    secret_number = number_picker()
    attempts = 10
    print(art.logo)
    print("I'm thinking of a number between 1 and 100.")
    #print(f"(pssst... the number is {secret_number}.)\n")

    difficulty = input("Please specify your difficulty. \nType 'easy' or 'hard'.\n").lower()
    
    if difficulty == "hard":
        attempts = attempts - 5
    counter = 0
    isRight = False
    
    while attempts > 0 and isRight == False:
        
        print(f"\nYou have {attempts} attempts to pick the right number.")
        guessed_number = int(input("\nSo, what's your guess?\n"))
        counter += 1

        print(number_checker(guessed_number,secret_number))
        
        if guessed_number == secret_number:
            isRight = True
        
        attempts = attempts - 1

    if attempts > 0:
        print(f"\nYou won in {counter} tries.")
    else:
        print(f"\nSorry, you have {attempts} attempts left. You have lost. My number was {secret_number}.\n")

    if input("Would you like to play again?\n").lower() == "y":
        clear()
        number_guesser()
    else:
        clear()
        print(art.end_text + "\n\n" + art.logo)
        
number_guesser()
