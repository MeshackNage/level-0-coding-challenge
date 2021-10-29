def find_common_characters(string_1, string_2):
    common = []
    for char in string_1.lower():
        if char in string_2.lower():
            if char not in common:
                common.append(char)
    print("Common characters:", ', '.join(common))


find_common_characters("Eckard", "Berry")
