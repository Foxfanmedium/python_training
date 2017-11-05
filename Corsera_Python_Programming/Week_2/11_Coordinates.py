x = int(input())
y = int(input())
z = int(input())
w = int(input())

if x > 0 and y > 0:
    if z > 0 and w > 0:
        print("YES")
    else:
        print("NO")
if x > 0 and z > 0:
    if y < 0 and w < 0:
        print("YES")
    else:
        print("NO")
if y > 0 and w > 0:
    if x < 0 and z < 0:
        print("YES")
    else:
        if y < 0 and w < 0:
            if x < 0 and z < 0:
                print("YES")
else:
        print("NO")
