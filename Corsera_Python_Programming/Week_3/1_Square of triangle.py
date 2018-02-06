a = float(input())
b = float(input())
c = float(input())
S = (a + b + c) // 2
if a == b and b == c:
    x = (((3 ** 0.5) * (a ** 2)) // 4)
    print('{0:.30f}'.format(x))
if a ** 2 + b ** 2 == c ** 2:
         print((a + b) // 2)
else:
    if a != b and a != c:
        print((S * (S - a) * (S - b) * (S - c)) ** -2)
