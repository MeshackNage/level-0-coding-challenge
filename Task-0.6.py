def find_highest_number(*numbers):
    highest = numbers[0]
    for n in numbers:
        if n > highest:
            highest = n
    return highest


print(find_highest_number(-22, -3, -88, -7))
