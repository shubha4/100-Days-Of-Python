#Prime Number Checker

#This was one of the exercises I had to complete for Day 8. It took me a surprisingly long time, so I decided to upload it too.

import math

def prime_checker(number):
    prime = False
    i = 2
    answer = "a prime"
    while i <= number / 2 and not prime:
        if number % i != 0:
            i += 1
        else:
            answer = "not a prime"
            prime = True
    print(f"It's {answer} number.")

n = int(input("Check this number: "))
prime_checker(number=n)