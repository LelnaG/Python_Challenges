# function definitions:


def to_twentyfour(time1):
    if time1 == "12:00AM":
        new_time = "00:00"
    elif "AM" in time1:
        new_time = time1.replace("AM", " ")
    else:
        time1 = time1.replace("PM", " ").split(":")
        new_hour = int(time1[0])+12
        time1[0] = str(new_hour)
        time1.insert(1, ":")
        new_time = ''.join(time1)

    return new_time


def to_twelve(time2):
    time2 = time2.split(":")
    if int(time2[0]) <= 12 and int(time2[0]) != 0:
        time2.insert(1, ":")
        new_time2 = ''.join(time2).replace("\n", "AM") if time2[0] != "12" else ''.join(time2).replace("\n", "PM")
    elif int(time2[0]) > 12 and int(time2[0]):
        time2[0] = str(int(time2[0])-12)
        time2.insert(1, ":")
        new_time2 = ''.join(time2).replace("\n", "PM")

    else:
        time2[0] = "12"
        time2.insert(1,":")
        new_time2 = ''.join(time2).replace("\n", "AM")
    return new_time2
# end function definitions


# main


file = open("advanced_testcases.txt", "r")
line = file.readline()
while line:  # while file is reading
    if line == "\n" or line.startswith("#"):
        line = file.readline()
        continue
    if "PM" in line:
        print(to_twentyfour(line))
    elif "AM" in line:
        print(to_twentyfour(line))
    else:
        print(to_twelve(line))
    line = file.readline()


print("Bye!")
