# Strategy 4 - Solution 2

import re

from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    unique_letters = set()
    for letter in re.findall(r"[a-z]", sentence.lower()):
        unique_letters.add(letter)
    return len(unique_letters) == len(lowercase_letters)
