vowels = ['a', 'o', 'i', 'e', 'u']
word = input("Provide a word to search for vowels:")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
#==============================================================================================
# vowels = ['a', 'o', 'i', 'e', 'u']
# word = input("Provide a word to search for vowels:")
# found = {}
# for k in sorted(found):
#     print(k, 'was found', found[k], 'time(s).')




for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')



































