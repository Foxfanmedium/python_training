x = int(input())
# if x % 10 == 0:
#     print(str(x) + " " + 'korov')
# if x == 1:
#     print(str(x) + " " + 'korova')
# if x % 10 == 1 and x != 11:
#     print(str(x) + " " + 'korova')
# if x % 10 != 0 and x != 1:
#     print(str(x) + " " + 'korovy')

if x % 10 == 1 and x != 11:
    print(x, 'korova')
elif 2 <= x % 10 <= 4 and x // 10 != 1:
    print(x, 'korovy')
else:
    print(x, 'korov')
