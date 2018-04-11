n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) and (k % m == 0)):
    print("YES")
elif ((n*m)-k) % 2 == 0:
            print("YES")
else:
    print("NO")
