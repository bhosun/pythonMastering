import random

# function to reverse word
def reverse(word):
    i = len(word)
    reversed_word = ""

    while i > 0:
        reversed_word += word[i -1]
        i -= 1
    return reversed_word

# function to generate random word
def generate_word(word_length):
    letters_mask = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    random_word = ""
    i = 0
    while i < word_length:
        random_word += letters_mask[random.randint(0, 25)]
        i += 1
    return random_word

# main ask him to reverse word
while True:
    word_length = 5
    the_word = generate_word(word_length)
    reverse_word = reverse(the_word)

    answer = str(input("Reverse this word - " + the_word + " "))
    answer = answer.lower()

    if answer == reverse_word.lower():
        print("✅")
    else:
        print("✖")