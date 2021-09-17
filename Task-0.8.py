def number_to_time(number):
    hour = number // 60
    minute = number % 60
    return f'{hour}'+" " + "hour(s)"+" " + f'{minute}'+" "+"minutes"


print(number_to_time(71))
