# challenges found on reddit thread: https://www.reddit.com/r/learnpython/comments/4d2yl7
# /i_need_list_comprehension_exercises_to_drill/

# ------------------------ No. 1 -----------------------
# Use a dictionary comprehension to count the length of each word in a sentence

# answer = {k:len(k) for k in "Making up a sentence".split(" ")}
# print(answer)

# ------------------------ No. 2 -----------------------
# Use a nested list comprehension to find all of the numbers
# from 1-1000 that are divisible by any single digit besides 1 (2-9)

# answer = [[j for j in range(1, 1001) if j % i == 0] for i in range(2, 10)]
# print(answer)

# ------------------------ No. 3 ---------------------- For all the numbers 1-1000, use a nested list/dictionary
# comprehension to find the highest single digit any of the numbers is divisible by

answer = {digit: max([j for j in range(1, 10) if digit % j == 0]) for digit in range(1, 1001)}
print(answer)


