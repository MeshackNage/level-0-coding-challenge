def find_vowels(string):
    i = []
    vowels = "aeiou"
    for x in string:
        if x in vowels:
            if x not in i:
                i.append(x)
    return i


print(find_vowels(str.lower('Umuzi BOOT CAmp ')))
