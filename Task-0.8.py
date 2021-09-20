def number_to_time(number):
    time = ''
    while True:
        hour = number // 60
        minute = number % 60
        if hour <= 1:
            print(f'{hour}' + " " + "hour")
        else:
            print(f'{hour}' + " " + "hours")
        if minute <= 1:
            print(f'{minute}' + " " + "minute")
        else:
            print(f'{minute}' + " " + "minutes")
        return time


print(number_to_time(133))

