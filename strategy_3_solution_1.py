# Strategy 3 - Solution 1

from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    unique_letters = set()

    for char in sentence.lower():
        if char.isalpha():
            unique_letters.add(char)
    return unique_letters == set(lowercase_letters)
