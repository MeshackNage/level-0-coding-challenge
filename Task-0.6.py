def maximum_num(*numbers):
    highest = numbers[0]
    for n in numbers:
        if n > highest:
            highest = n
    return highest


print(maximum_num(-22, -3, -88, -7))
