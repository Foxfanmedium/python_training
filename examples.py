# mylist = [1,2,3]
# for i in mylist:
#     print(i)

# mylist = [x*x for x in range(5)]
# for i in mylist:
#     print(i)
# print(mylist)

# def createGenerator():
#     mylist = range(3)
#     for i in mylist:
#         yield i *i
#
# mygenerator = createGenerator()
# print(mygenerator)
# for i in mygenerator:
#     print(i)

import itertools

horses = [1,2,3,4,5,6]

races = itertools.permutations(horses)
print(races)
print(list(itertools.permutations(horses)))






