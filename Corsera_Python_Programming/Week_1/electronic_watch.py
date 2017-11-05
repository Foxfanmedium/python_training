# n = int(input())
# print((n // 60 % 24), (n % 60))
n = int(input())
hours = n // 60 % 24
minutes = n % 60

print(hours, minutes)
