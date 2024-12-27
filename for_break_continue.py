numbers = [12, 75, 150, 180, 145, 501, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)


numbers = [2, 3, 6, 7, 10, 14, 50]
for item in numbers:
    if item > 10:
        break
    elif item > 7:
        continue
    # check if number is divisible by 2
    elif item % 2 == 0:
        print(item)