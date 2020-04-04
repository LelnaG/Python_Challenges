# time2 = " 03:00"
# time2 = time2.split(":")
# if int(time2[0]) < 12:
#     print("Lelna")

file = open("advanced_testcases.txt", "r")
line = file.readline()
while line:  # while file is reading
    line = file.readline()
    if line == "\n" or line.startswith("#"):
        continue