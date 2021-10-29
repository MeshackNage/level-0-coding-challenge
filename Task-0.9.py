def find_vowels(string):
    found_vowels = []

    for vowel in string.lower():
        if vowel in 'aeiou':
            if vowel not in found_vowels:
                found_vowels.append(vowel)
    print("Vowels:", ', '.join(found_vowels))


find_vowels('Umuzi BOOT CAmp ')
