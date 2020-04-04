input_string = input("Enter an AB sequence: ")

countA = 0
countB = 0

for letter in input_string:
    if letter == "A":
        countA += 1
    else:
        countB += 1

print("True") if countA == countB else print("False")