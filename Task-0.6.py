def maximum_num(*numbers):
    highest = 0
    for n in numbers:
        if n > highest:
            highest = n
    return highest


print(maximum_num(1, 22, 3, 2, 88))
