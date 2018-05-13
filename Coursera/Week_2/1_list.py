# empty_list = []
# empty_list = list()
# none_list = [None] * 10
# collections = ['list', 'tuple', 'dict', 'set']
# print(len(collections)) # >>> 4
# print(collections[0])
# print(collections[-1])
# collections[3] = 'frozenset'
# print(collections)
#
# print('tuple' in collections) #>>> True
##=====================================================================================================================
# range_list = list(range(10))
# print(range_list) # >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# collections = ['list', 'tuple', 'dict', 'set']
# for collection in collections:
#     print('Learning {}...'.format(collection))
#
# for idx, collection in enumerate(collections):
#     print('#{} {}'.format(idx, collection))
#=====================================================================================================================
# collections = ['list', 'tuple', 'dict', 'set']
# collections.append('OrderedDict')
# print(collections)
#
# collections.extend(['polyset', 'unicorndict'])
# print(collections)
#
# collections += [None]
#
# print(collections)
#
# del collections[7]
# print(collections)
#=====================================================================================================================
# numbers = [4, 17, 19, 9, 2, 6, 10, 13]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
#=====================================================================================================================
# tag_list = ['python', 'course', 'coursera']
# print(', '.join(tag_list))
#=====================================================================================================================
# import random
#
# numbers = []
# for _ in range(10):
#     numbers.append(random.randint(1,20))
# print(numbers)
#
# print(sorted(numbers)) # создается НОВЫЙ список!
# print(sorted(numbers, reverse=True)) # создается НОВЫЙ список!
#
# numbers.sort()
# print(numbers) # сортируется оригинальный список!
# numbers.sort(reverse=True)
# print(numbers) # сортируется оригинальный список!
#=====================================================================================================================
empty_tuple = ()
empty_tuple = tuple()
immutables = (int, str, tuple)

blink = ([], [])
blink[0].append(0) # кортеж не изменяем, но список внутри кортежа можно изменить
print(blink)

print(hash(tuple()))
#=====================================================================================================================