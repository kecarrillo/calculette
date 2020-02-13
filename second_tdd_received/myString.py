import random
import string


def start():
    lower_upper_alphabet = string.ascii_letters
    random_letter = []
    for x in range(50, 1000):
        for r_letter in range(0, x):

            random_letter += random.choice( lower_upper_alphabet )

    return random_letter


def tri(letters):
    lister = ["a", "e", "i", "o", "u", "y"]
    result = []
    for x in letters:
        if x in lister:
            result.append(x)
    return result

tri(start())
