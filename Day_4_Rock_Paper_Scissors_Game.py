#Here, I have made a rock, paper, scissors game that takes in input from users and generates random computer choices.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Hello there and welcome to the Rock, Paper and Scissors game! You can use this simulation to make the simplest life decisions, such as where do you want to eat, if you are as indecisive as me :) ")
user_choice = input("What do you hedge your bets on? Type '0' for Rock, '1' for Paper, or '2' for Scissors.\n")

user_choice = int(user_choice)

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  choices = [rock, paper, scissors]
  
  computer_choice = random.randint(0, 2)
  
  print(choices[user_choice] + "\nComputer chose:\n" + choices[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose :(")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice > user_choice:
    print("You lose :(")
  elif user_choice == computer_choice: 
    print("It's a draw!")