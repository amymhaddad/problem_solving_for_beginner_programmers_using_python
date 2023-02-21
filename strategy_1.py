# Strategy 1 - Solution

from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):

    letters_found = len(lowercase_letters) * [0]

    for char in sentence.lower():
        if char.isalpha():
            letter_index = ord(char) - ord("a")
            letters_found[letter_index] = 1

    return sum(letters_found) == len(lowercase_letters)
