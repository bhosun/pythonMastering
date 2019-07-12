count = True
while count:
    word = input("Input a word or sentence you want to reverse? ")
    stringed_word = str(word)
    i = len(stringed_word)
    reversed_word = ""

    while i > 0:
        reversed_word += stringed_word[i - 1]
        i -= 1
    print(reversed_word)
    count = False