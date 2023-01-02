#Blackjack Game

#Here, I have created a Blackjack game where the user can play against the computer as their opponent.

import os
import random
from blackjack_art import logo

clear = lambda: os.system('clear')

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards_list):
    """Takes in a list of cards and returns the score calculated from the list."""
    total = sum(cards_list)
    if len(cards_list) == 2 and total == 21:
        return 0
    elif (11 in cards_list) and total > 21:
        cards_list.remove(11)
        cards_list.append(1)
        total = sum(cards_list)
    return total

def compare(player_score, computer_score):
    """Compares player and computer scores."""
    if player_score == computer_score:
        return "You and the opponent have the same score. You draw 🤝🏼"
    elif computer_score == 0:
        return "The opponent has a blackjack. You lose 😵‍💫"
    elif player_score == 0:
        return "You win with a blackjack 🤩"
    elif player_score > 21:
        return "You went over 21. You lose 😱"
    elif computer_score > 21:
        return "The opponent went over 21. You win 😜"
    elif player_score > computer_score:
        return "You win 🥳"
    else:
        return "You lose 😭"

def hand(p_cards, c_cards):
    print(f"\tYour cards: {p_cards}, current score: {calculate_score(p_cards)}")
    print(f"\tComputer's first card: {c_cards[0]}")

def final_hand(p_cards, c_cards):
    print(f"\tYour final hand: {p_cards}, final score: {calculate_score(p_cards)}")
    print(f"\tComputer's final hand: {c_cards}, final score: {calculate_score(c_cards)}")
          

def game_play():
    game_end = False
    print(logo)
    player_cards = []
    computer_cards = []
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    hand(player_cards, computer_cards)
    while not game_end:
        if calculate_score(player_cards) > 21 or calculate_score(player_cards) == 0 or calculate_score(computer_cards) == 0 :
            game_end = True
            final_hand(player_cards, computer_cards)
            print(compare(calculate_score(player_cards), calculate_score(computer_cards)))
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == "y":
                player_cards.append(deal_card())
                hand(player_cards, computer_cards)
                while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
                    computer_cards.append(deal_card())
            else:
                game_end = True
                final_hand(player_cards, computer_cards)
                print(compare(calculate_score(player_cards), calculate_score(computer_cards)))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    clear()
    game_play()
        
    