n = int(input())
while n >= 0:
    if n == 1:
        print(n)
        break
    else:
        n =1 + (1 / ((n - 1) ** 2))+ (1 / ((n + 1) ** 2))
        print(n)
        break
