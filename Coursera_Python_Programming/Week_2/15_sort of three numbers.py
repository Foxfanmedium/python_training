a = int(input())
b = int(input())
c = int(input())

if a > b > c:
    print('a', 'b', 'c')
if b > a > c:
    print('b', 'a', 'c')
if c > a > b:
    print('c', 'a', 'b')
if c > b > c:
    print('c', 'b', 'a')