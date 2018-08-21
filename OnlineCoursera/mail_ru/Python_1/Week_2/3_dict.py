# empty_dict = {}
# empty_dict = dict()
#
# collection_map = {
#     'mutable':['list', 'set', 'dict'],
#     'immutable': ['tuple', 'frozenset']
# }
# print(collection_map['immutable'])
#
# print(collection_map.get('irresistible', 'not found')) # -> Возвращение сообщения если не найден ключ
#
# if 'mutable' in collection_map:
#     print(True)
#
# print('mutable' in collection_map)
#==============================================================
# beatles_map = {
#     'Paul':'Bass',
#     'John':'Guitar',
#     'George':'Guitar'
# }
# beatles_map['Ringo'] = 'Drums'
# print(beatles_map)
#
# del beatles_map['John']
# print(beatles_map)
#
# beatles_map.update({'John':'Guitar'})
# print(beatles_map)
#
# print(beatles_map.pop('Ringo'))
#==============================================================
# unknown_dict = {}
# print(unknown_dict.setdefault('key', 'default'))
# print(unknown_dict)

#==============================================================
# collection_map = {
#     'mutable':['list', 'set', 'dict'],
#     'immutable': ['tuple', 'frozenset']
# }
# print(collection_map)
# for key in collection_map:
#     print(key)
#
#
# for key, value in collection_map.items():
#     # print(key, value)
#     print('{} is for {}'.format(key, value))
#
# for value in collection_map.values():
#     print(value)
#==============================================================
from collections import OrderedDict

ordered = OrderedDict()

for number in range(10):
    ordered[number] = str((number))
for key in ordered:
    print(key)
    print(ordered)






