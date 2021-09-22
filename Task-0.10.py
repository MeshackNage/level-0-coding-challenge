def common_characters(string_1, string_2):
    common = []
    i = ""
    for x in string_1 or string_2:
        if x in string_1:
            common.append(x.lower())
    print("Common characters:", ', '.join(common))
    return i


print(common_characters("Ear", "Dear"))
