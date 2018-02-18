a = [1,2,3,4,5]
b = [10,20,30,40,50]
c = [100,200,300,400,500]

args = [a, b, c]

result = list(zip(a, b, c))
# result = list(zip(*args))
print(result)
print(*result)
