#  Неизменяемые типы данных
a = 4
b = 5
c = 'abcd'
e = True
f = (1, 2, 3, 4)
g = 4.4

def test(some_data):
    some_data = 100

test(a)
print(test(a))


