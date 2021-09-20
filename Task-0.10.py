def common_characters(string_1, string_2):
    common = []
    for x in string_1:
        if x in string_2:
            common.append(x)

    return "Common character: ", *common


print(common_characters("meshack", "nage"))
