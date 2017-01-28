def alphabet_position(letter):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    letter_index=alphabet.index(letter.lower())
    return letter_index

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted=''
    index1=alphabet_position(char)
    rotated_index = index1 + rot
    if rotated_index < 26:
        encrypted = encrypted + alphabet[rotated_index]
    else:
        encrypted = encrypted + alphabet[rotated_index % 26]
    if char.istitle():
        return encrypted.upper()
    else:
        return encrypted

def encrypt(text, rot):
    encrypted=''
    for char in text:
        if char.isalpha():
            encrypted=encrypted+rotate_character(char, rot)

        else:
            encrypted=encrypted+char

    return encrypted
