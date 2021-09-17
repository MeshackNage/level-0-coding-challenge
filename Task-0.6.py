def maximum(*numbers):
    highest = sorted(numbers, reverse=True)
    return highest[0]


print(maximum(1, 22, 3, 2))
