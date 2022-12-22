#Here, I have created a tip calculator that takes in the amount of you bill, the tip percentage of your choosing, and the number of people in your party.
#It then provides the total amount each person should pay.

amount = input("Hiya there! Welcome to the tip calculator, where I do all the fun calculations for you :)\nWhat was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 15, 20, or 25? ")
num_people = input("How many people to split the bill with? ")

amount = float(amount)
tip_percentage = float(tip_percentage)
num_people = int(num_people)

total_amount = amount + amount * (tip_percentage/100)
per_person_amount = total_amount/num_people
per_person_amount = "{:.2f}".format(per_person_amount)

message = f"Each person should pay: ${per_person_amount}"

print(message)