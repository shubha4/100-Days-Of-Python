#Number Guesser Game

#Here, I have created a number guessing game that randomly generates a number between 1-100 and allows the user to guess it in either the hard or easy mode.
import os
from random import randint
from numguess_art import logo

clear = lambda: os.system('clear')

def attempt_calc():
    option = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if option == "easy":
        return 10
    else:
        return 5

def num_generator():
    return randint(1, 100)

def game_play(attempts):
    clear()
    game_end = False
    while attempts > 0 and not game_end:
        player_guess = int(input(f"\nYou have {attempts} attempts remaining to guess the number.\nMake a guess: "))
        if player_guess > game_num:
            print("Too high.")
        elif player_guess < game_num:
            print("Too low.")
        elif player_guess == game_num:
            print(f"You got it! The answer is {game_num}")
            game_end = True
        attempts -= 1
        if attempts == 0 and player_guess != game_num:
            print("You have run out of guesses, you lose.")
            print(f"The number was {game_num}")
        elif player_guess != game_num:
            print("Guess again!")

print(logo)
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")

num_attempts = attempt_calc()
game_num = num_generator()
game_play(num_attempts)