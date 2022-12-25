#Password Generator

#Here, I have created a password generator that takes in values from the user about the number of letters, numbers and symbols they would like their password to have.
#The program then generates password and randomized the order in which the letters, numbers and symbols appear.

import random
from random import sample 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Create a list of randomized characters as requested by the user. 
password_asList = []

for letter in range(1, nr_letters + 1):
  password_asList.append(random.choice(letters))
for symbol in range(1, nr_symbols + 1):
  password_asList.append(random.choice(symbols))
for number in range(1, nr_numbers + 1):
  password_asList.append(random.choice(numbers))

#Shuffle the list without replacing
password_asList = sample(password_asList, len(password_asList))

#Convert the list into a string
randomized_password = ""

for i in password_asList:
  randomized_password += i

print("Your password is: " + randomized_password)