# sentence = 'the quick brown fox jumps over the lazy dog'
# words = sentence.split()
# print(words)
# word_lenght = []
#
# for word in words:
#     word_lenght.append(len(word))
# print(word_lenght)
#======================================================================================================================
# sentence = 'the quick brown fox jumps over the lazy dog'
# words = sentence.split()
# word_lenght = [len(word) for word in words if word!='the']
# print(word_lenght)
#======================================================================================================================
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# newlist = [int(number) for number in numbers if number > 0]
# print(newlist)

list = [5, 10, -5, 80, -6, 102, -96, 23, 20, 56, 0, 12, 45, -8]
odd_list = [int(number) for number in list if number > 10]
print(odd_list)














