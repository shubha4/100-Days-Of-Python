#Silent Auction Project

#Here, I have designed a silent auction program that takes in values from the users and provides the name and bid of the auction winner.
#In the case of a draw, the person who put in the first bid will win. 

import os
from auction_art import logo

clear = lambda: os.system('clear')

#Import the logo and display the welcome message
print(logo)
print("Hello there! Welcome to the Silent Auction :)")

#Function to add participants and their bids to dictionaries within a list
participant_info = []
def bid_entry(participant_name, participant_bid):
    participant_info.append(
        {
            "name": participant_name,
            "bid": participant_bid
        }
    )

#Function to find and display the highest bidder and their bid
def find_highest_bidder(bidding_record):
    highest_bid = 0
    highest_bidder = ""
    for entry in range(len(bidding_record)):
        current_bid = int(bidding_record[entry]["bid"])
        current_bidder = bidding_record[entry]["name"]
        if current_bid > highest_bid:
            highest_bid = current_bid
            highest_bidder = current_bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


another_person = True

#While loop to take in values from multiple users
while another_person:
    name = input("What is your name? ")
    bid = input("What is your bid today? $")
    bid_entry(name, bid)
    go_again = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if go_again == "no":
        another_person = False
    else:
        clear()

find_highest_bidder(participant_info)
