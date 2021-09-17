def celsius_to_fahrenheit(temp_cel):
    temp_ft = str((temp_cel * 1.8) + 32)
    print("Temperature in Fahrenheit is: ")
    return temp_ft


print(celsius_to_fahrenheit(44))


def fahrenheit_to_celsius(temp_ft):
    temp_cel = str((temp_ft - 32) * 5/9)
    print("Temperature in Celsius is: ")
    return temp_cel


print(fahrenheit_to_celsius(111))
