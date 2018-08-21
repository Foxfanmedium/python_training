# phrase = "Don't panic!"
# plist = list(phrase)
# letter = ['D', 'a', 'n', 'i', 'c', '!', ' ', 'n']
# plist.pop(3)
# for vobl in letter:
#     plist.remove(vobl)
# plist.insert(1, 'n')
# plist.insert(2, ' ')
# plist.insert(4, 'a')
# new_phrase = ''.join(plist)
# print(new_phrase)
#==============================================================================================
# phrase = "Don`t panic!"
# plist = list(phrase)
# for i in range(4):
#     plist.pop()
# plist.pop(0)
# plist.remove("`")
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))
# new_phrase = ''.join(plist)
# print(new_phrase)
#==============================================================================================
# string = "The Hitchhiker's Guide to the Galaxy"
# backwards = string[::-1]
# print(backwards)
# string_1 = "The Hitchhiker's Guide to the Galaxy"
# backwards_1 = string_1[::2]
# print(backwards_1)
#==============================================================================================

phrase = "Don`t panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])
print(new_phrase)

















