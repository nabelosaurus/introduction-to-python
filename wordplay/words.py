import string

import scrabble


vowels = ['a', 'e', 'i', 'o', 'u']
# for word in scrabble.wordlist:
#     if "dq" in word and "xu" not in word:
#         print(word)


def has_a_double(letter):
    doubled = letter + letter
    for word in scrabble.wordlist:
        if doubled in word:
            return True
    return False


def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True


for letter in string.ascii_lowercase:
    if not has_a_double(letter):
        print(letter)

# counter = 0
# for word in scrabble.wordlist:
#     if has_all_vowels(word):
#         counter += 1
#         print(word)

# print(counter)
