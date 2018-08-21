vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget to pack your towel"

found = set()
for v in vowels:
    if v in message:
        found.add(v)

found2 = {v for v in vowels if v in message}

print(found)
print(found2)








