#Higher Lower Game

#Here, I have created a program that allows the users to guess which Instagram account has more followers and see if they are correct.

import random
import os
from game_data import data
from higher_lower_art import logo, vs

clear = lambda: os.system('clear')

def character_details():
    """Provides a random value from the data list."""
    return random.choice(data)

def character_introduction(first_char, second_char):
    """Gives an overview of the account and gets user input."""
    print(
        f"Compare A: {first_char['name']}, a {first_char['description']}, from {first_char['country']}."
    )
    print(vs)
    print(
        f"Against B: {second_char['name']}, a {second_char['description']}, from {second_char['country']}."
    )
    return input("Who has more followers? Type 'A' or 'B': ").lower()

def compare(guess, first_char, second_char):
    """Compares the follower counts of the two accounts and checks if the user is correct. """
    if first_char['follower_count'] > second_char['follower_count']:
        return guess == "a"
    else:
        return guess == "b"

def game_play():
    print(logo)
    score = 0
    game_end = False
    first_character = character_details()
    second_character = character_details()

    while not game_end:
        first_character = second_character
        second_character = character_details()
        
        while first_character == second_character:
            second_character = character_details()
        
        guess = character_introduction(first_character, second_character)

        is_correct = compare(guess, first_character, second_character)

        clear()
        print(logo)
            
        if is_correct:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            game_end = True
            print(f"Sorry, that's wrong. Final score: {score}")
            

game_play()