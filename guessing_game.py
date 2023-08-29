"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

import random
from statistics import mean, mode, median

RANGE_NUMBER = 100


def separator():
    # function that displays a separator in terminal
    print("*" * 50)
    print()


def print_results(list):
    # function that displays the stats on the attempts
    print(f"""
        number of attempts = {len(list)} 
        mean = {round(mean(list), 2)}
        mode = {mode(list)}
        median = {median(list)}""")


def start_game():
    # main program

    # welcome
    print("\nWelcome to our Number Guessing Game !\n")
    name = input("what is your name?   ").capitalize()
    separator()

    winning_number = random.randint(0, RANGE_NUMBER)
    attempts = []
    highest_score = 100

    # continuous guess prompting
    while True:
        guess = input(
            f"{name}, enter a number between 0 and 100:   ")

        try:
            guess = int(guess)
            # out of range feedback
            if guess > 100 or guess < 0:
                raise ValueError("The number has to be between 0 and 100.")
        except ValueError as err:
            if "base 10" in str(err):
                print(f"{name}, you have to enter a number.")
                separator()
            else:
                print(err)
                separator()
        else:
            # attempts is a list of the guess inputs
            attempts.append(guess)

            if guess == winning_number:
                separator()
                print("******** Got it ********")

                # display the highest score
                if len(attempts) <= highest_score:
                    highest_score = len(attempts)

                print_results(attempts)
                print(f"The highest score is {highest_score}")
                separator()

                still_playing = input("Do you want to continue? Y/N     ")

                # prompt the user for continuing to play or not
                if still_playing.lower() == 'y':
                    attempts = []
                    winning_number = random.randint(0, 100)
                else:
                    print(
                        f"Goodbye {name}! Your highest score was {highest_score} attempts to guess a number.")
                    break

            elif guess > winning_number:
                print("It's lower")
                separator()
                continue

            elif guess < winning_number:
                print("It's higher")
                separator()
                continue


start_game()
