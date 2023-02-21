# Strategy 2 - Solution

from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    for letter in lowercase_letters:
        if letter not in sentence.lower():
            return False
    return True
