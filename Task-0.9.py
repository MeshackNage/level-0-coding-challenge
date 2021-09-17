def find_vowels(string):
    i = ""
    vowels = "a", "e", "i", "o", "u"
    for x in string:
        if x in vowels:
            i += x
    return i


print(find_vowels('Umuzi'))
