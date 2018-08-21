# empty_list = []
# empty_list = list()
# none_list = [None] * 10
# collections = ['list', 'tuple', 'dict', 'set']
# user_data = [
#     ['Elena', 4.4],
#     ['Andrey', 4.2]
# ]
# print(len(collections))
# print(collections)
# print(collections[0])
# print(collections[1])
#
# collections[3] = 'frosenset'
# print(collections)
# # print(collections[10])
#
# if 'tuple' in collections:
#     print('True')
# print('tuple' in collections)
#===============================================================
# range_list = list(range(10))
# print(range_list)
#
# print(range_list[1:3]) #->[1, 2]
# print(range_list[3:]) #->[3, 4, 5, 6, 7, 8, 9]
# print(range_list[:7]) #->[0, 1, 2, 3, 4, 5, 6]
# print(range_list[::2])#->[0, 2, 4, 6, 8]
# print(range_list[::-1])#->[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#===============================================================

collections = ['list', 'tuple', 'dict', 'set']

for collection in collections:
    print('Learning {}...'.format(collection))

for idx, collection in enumerate(collections):
    print('#{} {} '.format(idx, collection))
#===============================================================
# collections = ['list', 'tuple', 'dict', 'set']
# collections.append('Ordered_dict')
# print(collections)
#
# collections.extend(['ponyset','unicorndict']) # расш ирение исходного списка другим списком
# print(collections)
#
# collections += [None]
# print(collections)
#
# del collections[4]
# print(collections)
#===============================================================
# numbers = [4, 17, 19, 9, 2, 6, 10, 13]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# tag_list = ['python', 'course', 'coursera']
# print(', '.join(tag_list)) #->python, course, coursera

# import  random
# numbers = []
#
# for _ in range(10):
#     numbers.append(random.randint(1,20))
# print(numbers)
#
# print(sorted(numbers))
# print(numbers)
# print(sorted(numbers, reverse=True))
# print(numbers)
#
#
# numbers.sort() #-> сортировка чисел в исходном списке, а не создание нового
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
#===============================================================
# empty_tuple = ()
# empty_tuple = tuple()
# immutables = (int, str, tuple)
#
# blink = ([], [])
# blink[0].append(0)
# print(blink)
#
# print(hash(tuple()))
#===============================================================











