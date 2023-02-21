# Strategy 3 - Solution 2


def is_pangram(sentence):

    actual_bits = 0

    expected_bits = 0b11111111111111111111111111

    for _, char in enumerate(sentence):
        if char.isalpha():
            letter_index = ord(char.lower()) - ord("a")
            bit_shift = 1 << letter_index
            actual_bits = actual_bits | bit_shift

    return expected_bits == actual_bits
