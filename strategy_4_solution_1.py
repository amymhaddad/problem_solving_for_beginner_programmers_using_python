# Strategy 4 - Solution 1

import re


def is_pangram(sentence):
    return len(set(letter for letter in re.findall(r"[a-z]", sentence.lower()))) == 26
