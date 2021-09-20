def find_vowels(string):
    i = []
    x = ''
    vowels = "aeiou"
    for x in string:
        if x in vowels:
            if x not in i:
                i.append(x)
    print("Vowels:", *i)
    return x


print(find_vowels(str.lower('Umuzi BOOT CAmp ')))
