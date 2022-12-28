#Caesar Cipher

#Here, I have created a Caesar Cipher tool that has the ability to cipher and decipher all alphabets and numbers, as well as most symbols.

import caesar_art

print(caesar_art.logo)

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+']

def caesar(start_text, shift_amount, cipher_direction):
    
    result_text = ""
    
    for char in start_text:
        if char not in characters:
            result_text += char
        else:
            letter_index = characters.index(char)
            if cipher_direction == "encode":
                if (letter_index + shift_amount) > len(characters) - 1:
                    shifted_letter = characters[(letter_index + shift_amount) - 45]
                else:
                    shifted_letter = characters[letter_index + shift_amount]
                result_text += shifted_letter
            else:
                if (letter_index - shift_amount) < 0:
                    shifted_letter = characters[45 - (shift_amount - letter_index)]
                else:
                    shifted_letter = characters[letter_index - shift_amount]
                result_text += shifted_letter
    print(f"Here's the {cipher_direction}d result: {result_text}")

should_continue = True

while should_continue:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 45:
        shift = shift % 45
    
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    another_go = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if another_go == "no":
        should_continue = False

print("Goodbye👋")