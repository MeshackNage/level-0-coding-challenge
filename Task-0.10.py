def common_characters(string_1, string_2):
    common = []
    if len(string_1) > len(string_2):
        for x in string_1:
            if x in string_2:
                common.append(x)
    else:
        for x in string_2:
            common.append(x)
    return "Common character: ", *common


common_characters("meshack", "nage")
