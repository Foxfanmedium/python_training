x = int(input())
y = int(input())
if x > y:
    print(1)
if y > x or y == 0:
    print(2)
elif x == y:
    print(0)
