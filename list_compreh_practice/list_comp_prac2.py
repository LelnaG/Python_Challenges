# drills found on reddit thread: https://www.reddit.com/r/learnpython/comments/4d2yl7
# /i_need_list_comprehension_exercises_to_drill/

# -------------------- No. 1 -------------------
# Find all of the numbers from 1-1000 that are divisible by 7

# answer = [number for number in range(1,1001) if number%7 == 0]
# print(answer)

# ------------------- No. 2 --------------------
# Find all of the numbers from 1-1000 that have a 3 in them

# answer = [number for number in range(1, 1001) if "3" in str(number)]
# print(answer)

# -------------------- No.3 ---------------------
# Count the number of spaces in a string

answer = [space for space in "I like to eat" if space == " "]
print(len(answer))

# -------------------- No. 4 --------------------
# Remove all of the vowels in a string

answer = [vowel for vowel in "Lelna" if vowel in "AEIOUaeiou"]
print(answer)

# -------------------- No. 5 --------------------
# Find all of the words in a string that are less than 4 letters

answer = [word for word in "I ate pizza on saturday".split(" ") if len(word) < 4]
print(answer)
