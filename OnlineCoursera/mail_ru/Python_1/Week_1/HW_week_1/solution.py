import sys

digit_string = sys.argv[1]
result = []

for num in digit_string:
    result.append(int(num))
    summ = sum(result)
print(summ)