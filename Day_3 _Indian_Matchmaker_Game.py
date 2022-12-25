#Indian Matchmaker Quiz

#Here, I have created a game based on Netflix's iconic TV show, The Indian Matchmaker.
#Based on your chosen options, you will be matched with one of the cast members!

print('''
                                   d8b                         
                                   Y8P                         
                                                               
88888b.d88b.  8888b. 888d888888d888888 8888b.  .d88b.  .d88b.  
888 "888 "88b    "88b888P"  888P"  888    "88bd88P"88bd8P  Y8b 
888  888  888.d888888888    888    888.d888888888  88888888888 
888  888  888888  888888    888    888888  888Y88b 888Y8b.     
888  888  888"Y888888888    888    888"Y888888 "Y88888 "Y8888  
                                                   888         
                                              Y8b d88P         
                                               "Y88P"     
''')

print("Welcome to Seema Auntie's Treasure Island! Where we don't know if you will find a treasure but you will certainly learn how to 'settle'!")
print("You mission is to find your Indian soulmate :)")

coffee = input("You are at a cross road. On one end you see a Starbucks and the other you see a Dunkin Donuts. Where are you going to get your coffee? Type 'S' or 'D'.\n").lower()

if coffee == "s":
    activity = input("In your free time, what do you envision yourself doing? Doing yoga, mixing cocktails, traveling, or playing animal crossing? Type 'Y', 'C', 'T', or 'A'.\n").lower()
    if activity == "y":
        print("Congrats! You are matched with Nadia. Enjoy your time with the sweet bubbly queen, who will probably start hounding you for kids in the next 6 months!")
    elif activity == "c":
        print("Congrats! You are matched with Pradhyuman. You are the 'diamond of the first water' because the dude has rejected 150 women, and you are the CHOSEN one! Plus, we were sick of finding him matches.")
    elif activity == "t":
        print("Congrats! You are matched with Viral. Our queen has high aspirations and even higher expectations. Be ready to confront your mommy issues, because she has the knack of bringing them out!")
    else:
        shubha_choice = input("You were matched with your truly! But first things first, do you like dogs and is your name Gavin? Type 'Y' or 'N'.\n").lower()
        if shubha_choice == "y":
            print("YOU HAVE WON THE PRIZE!! Get ready for a snack-loving, low-key grouchy, and beautiful partner <3.")
        else:
            print("Shubha says, 'Thank you for your interest, but we will be moving forward with other qualified candidates.'")
else: 
    boring = input("Do you enjoy going out with your friends or staying at home and reading? Type 'O' or 'R'.\n").lower()
    if boring == "o":
        print("Congrats! You are matched with Akshay. Who can beat a balding head, unearned self-confidence, and a million chicken stories?")
    else:
        print("Congrats! You are matched with Aparna. You will fall in love with her iconic side-eye and ability to yawn at the most inopportune times.")
