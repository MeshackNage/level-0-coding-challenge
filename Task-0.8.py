def number_to_time(number):
    hour = number // 60
    minute = number % 60
    m = "minute"
    h = "hour"
    if hour > 1:
        h += "s"
    if minute > 1:
        m += "s"
    print(f'{hour} {h}  {minute} {m}')


number_to_time(71)

