# Original solution

from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    letters_found = ""

    for char in sentence.lower():
        if char.isalpha() and char not in letters_found:
            letters_found += char
    return len(letters_found) == len(lowercase_letters)
