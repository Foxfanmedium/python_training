A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A * B <= D * E or A * C <= D * E or B * C <= D * E:
    print("YES")
else:
    print("NO")
