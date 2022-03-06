def lowercase_letter_rotation(plain_letter, rotational_shift):
    current_letter_ord = ord(plain_letter)
    new_letter_ord = current_letter_ord + rotational_shift - 97 # the new character's unicode, zero-indexed.
    substitute = alphabet[new_letter_ord % 26] # the new letter in the English alphabet   
    return(substitute) 

def uppercase_letter_rotation(plain_letter, rotational_shift):
    current_letter_ord = ord(plain_letter)
    new_letter_ord = current_letter_ord + rotational_shift - 65 # the new character's unicode, zero-indexed.
    substitute = alphabet_caps[new_letter_ord % 26] # the new letter in the English alphabet   
    return(substitute) 

def caesar_cipher(plaintext, key, all_lowercase = False, all_uppercase = False):

# Verification needed that the key is an int and not a string.
    #(Coming soon)

    ciphered_text = []
    size_of_plaintext = len(plaintext)

    for i in range(size_of_plaintext):

        current_letter = plaintext[i]

        # Checks to see what type of character it is.
        current_letter_ord = ord(current_letter)

        # If it's a space, the cipher leaves it alone.
        # If it's anything other than a letter, space or period, it throws an error.

        # uppercase letters
        if current_letter_ord >= 65 and current_letter_ord <= 90:
            substitute = uppercase_letter_rotation(current_letter, key)
            ciphered_text.append(substitute)

        # lowercase letters
        elif current_letter_ord >= 97 and current_letter_ord <= 122:
            substitute = lowercase_letter_rotation(current_letter, key)
            ciphered_text.append(substitute)

        # space or period, respectively
        elif current_letter_ord == 32 or current_letter_ord == 46:
            ciphered_text.append(current_letter) # no changes necessary

        # not a valid character.
        else:
            # throw an error
            continue

# if all_lowercase is true, return plaintext in all lowercase

# if all_uppercase is true, return plaintext in all uppercase

    return ''.join(ciphered_text) # converts the list to a string

# The Vignere Cipher is a polyalphabetic extension of the Caesar Cipher.
def vignere_cipher(plaintext, key, all_lowercase = False, all_uppercase = False):

    # Verify that the key is actually a valid string and not something else 
    # (like an int or a phrase that includes non-alphabetic characters).
    #(Coming soon)

    ciphered_text = []

    # Convert the string into a list of letters and perform the correct
    # substitution on each depending on its position.
    poly_sub_in_motion = True
    counter = 0
    size_of_plaintext = len(plaintext)

    while (poly_sub_in_motion):

        # Perform a check to see if we're at the end of the string (or if the string is empty).
        if(counter == size_of_plaintext):
            break

        current_letter = plaintext[counter]

        # Convert the current letter in the Vignere key to an ordinal
        # to cipher the current plaintext letter.
        current_vignere_letter = key[counter % len(key)]
        current_vignere_ord = ord(current_vignere_letter)

        # Currently the ordinal is within ranges 65 - 90 and 97 - 122.
        # Convert it into a range of 0 - 25 before proceeding.
        if current_vignere_ord >= 65 and current_vignere_ord <= 90:
            poly_rotation = current_vignere_ord - 65
        elif current_vignere_ord >= 97 and current_vignere_ord <= 122:
            poly_rotation = current_vignere_ord - 97

        # Perform the Caesar Cipher on the letter.
        ciphered_text.append(caesar_cipher(current_letter, poly_rotation))

        counter += 1
    
    return ''.join(ciphered_text) # converts the list to a string

alphabet_caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 65-90
alphabet = 'abcdefghijklmnopqrstuvwxyz' # 97-122

phrase = 'sEcReTMesSAGE'
# caesar_key = 5
vignere_key = 'aPpLe'

# print("Output of Caesar Cipher with a shift of " + str(caesar_key) + " is " + caesar_cipher(phrase, caesar_key))
print("Output of Vignere Cipher with a shift of " + vignere_key + " is " + vignere_cipher(phrase, vignere_key))
