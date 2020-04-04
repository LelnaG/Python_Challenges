###Create a list of words that aren’t allowed to be in a sentence.
# Then given a user inputted string, check to see if any of the words that aren’t allowed appear in the string.
# Replace all instances of those words with “*”

invalid_words = ["strawberry", "yellow", "flag"]

file = open("intermediate_testcases", "r")

for sentence in file.readlines():
    new_sentence = ""
    sentence = sentence.split(" ")
    if sentence == ["\n"]:
        continue
    for word in sentence:
        if word in invalid_words:
            word = "*"
        new_sentence = new_sentence + word + " "
    print(new_sentence)

    # for word in sentence:
    #     if word in invalid_words:
    #         word = "*"
    #     print(sentence)


