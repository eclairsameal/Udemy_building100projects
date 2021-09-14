alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(start_text, shift_alphabet, cipher_direction):
    ans_text = ""
    if cipher_direction == "decode":
        shift_alphabet *= -1
    for letter in start_text:
        new_position = alphabet.index(letter) + shift_alphabet
        if new_position >= len(alphabet):
            new_position -= len(alphabet)
        ans_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {ans_text}")  

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_alphabet=shift, cipher_direction=direction)