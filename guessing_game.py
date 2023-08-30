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
        scores are = {list}
        number of games = {len(list)} 
        mean = {round(mean(list), 2)}
        mode = {mode(list)}
        median = {median(list)}""")


def start_game():
    # main program

    # welcome
    print("\nWelcome to our Number Guessing Game !\n")
    name = input("What is your name?   ").capitalize()
    separator()

    winning_number = random.randint(0, RANGE_NUMBER)
    scores = []
    tries = 0

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
            tries += 1

            if guess == winning_number:
                separator()
                print("******** Got it ********")

                # save current score in scores list
                scores.append(tries)

                print_results(scores)
                separator()

                still_playing = input("Do you want to continue? Y/N     ")

                # prompt the user for continuing to play or not
                if still_playing.lower() == 'y':
                    tries = 0
                    winning_number = random.randint(0, 100)
                    print(
                        f"The highest score is {min(scores)}. Do you think you can do better?")
                    separator()
                else:
                    print(
                        f"\nGoodbye {name}! Your highest score was {min(scores)} tries to guess a number.\n")
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
