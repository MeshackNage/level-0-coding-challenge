def common_characters(string_1, string_2):
    common = []
    i = ""
    for x in string_1:
        if x in string_2:
            common.append(x)
    print("Common characters:", ', '.join(common))
    return i


print(common_characters("house", "computers"))
