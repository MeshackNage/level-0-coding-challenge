def convert_number_to_time(number):
    hour = number // 60
    minute = number % 60
    minute_ = "minute"
    hour_ = "hour"
    if hour > 1:
        hour_ += "s"
    if minute > 1:
        minute_ += "s"
    print(f'{hour} {hour_}  {minute} {minute_}')


convert_number_to_time(71)

