def common_characters(string_1, string_2):
    common = []
    i = ""
    for x in string_1.lower():
        if x in string_2.lower():
            if x not in common:
                common.append(x)
    print("Common characters:", ', '.join(common))
    return i


common_characters("Eckard", "Berry")
