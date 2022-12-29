#Calculator

#Here, I have created a calculator program that uses recursion if the user wants to restart with a new calculation.

import os
from calc_art import logo

clear = lambda: os.system('clear')

#Addition
def add(n1, n2):
    return n1 + n2

#Subtraction
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1**n2

#Functions dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent,
    
} 

#Calculator function that outputs calculation results
def calculator():
    """Here, I used recursion to call the function again in the later if/else statements."""
    print(logo)
    
    num1 = float(input("What's your first number?: "))
    for operator in operations:
        print(operator)
    
    continue_operation = True
    while continue_operation: 
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's your next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        another_go = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or 'e' to exit.: ").lower()
        if another_go == "y":
            num1 = answer
        elif another_go == "n":
            continue_operation = False
            clear()
            calculator()
        else:
            continue_operation = False
        
calculator()