from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#have two alphabets in case we need to encrypt beyond z - it will loop back around to a

repeat = True

def caesar(plain_text, shift_amount, direction_val):
    end_text = ""
    if direction_val == "decode":
        shift_amount *= -1 #makes the integers negative if the value is decode, to subtract the shift later on
    for x in plain_text:
        if x.isalpha() == True: #checks if the character x is a letter
            position = alphabet.index(x) #finds the index of the letters that we're looping through in the alphabet
            new_position = position + shift_amount #creates the new index from the previous position + the shift
            end_text += alphabet[new_position] #finds the letter at the new indices and adds these letters to the cipher_text
        else: #if the charater x is not a letter it's true value is pushed to the end string with no shift
            end_text += x
    print(f"The {direction_val}d text is {end_text}")

while repeat == True: #asks the user if they'd like to run the shift again
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26: #if the user inputs a number greater than the number of letters in the alphabet (26)
        new_shift = shift % 26
        shift = new_shift

    caesar(plain_text = text, shift_amount = shift, direction_val = direction)

    user_val = input("Would you like to play again? (Y/N): ").upper()

    if user_val == "Y":
        repeat = True
    else:
        repeat = False
