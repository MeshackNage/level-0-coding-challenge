def find_common_characters(string_1, string_2):
    common = []
    for x in string_1.lower():
        if x in string_2.lower():
            if x not in common:
                common.append(x)
    print("Common characters:", ', '.join(common))


find_common_characters("Eckard", "Berry")
