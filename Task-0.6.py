def find_highest_number(*numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest


print(find_highest_number(-22, -3, -88, -7))
