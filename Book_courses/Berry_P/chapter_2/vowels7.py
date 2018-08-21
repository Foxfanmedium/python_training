# vowels = ['a', 'o', 'i', 'e', 'u']
# word = input("Provide a word to search for vowels:")
# found = []
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for vowel in found:
#     print(vowel)
#==================================================================
# vowels = ['a', 'o', 'i', 'e', 'u']
# word = input("Provide a word to search for vowels:")
# found = set(word)
# intersec = found.intersection(vowels)
# print(intersec)
#==================================================================
# Еще короче
vowels = set('aoieu')
word = input("Provide a word to search for vowels:")
found = vowels.intersection(set(word))
print(found)





