def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


import types

if type(fib()) == types.GeneratorType:
    print('Good, The fib function is generator')

    counter = 0
    list = []
    for n in fib():
        list.append(n)
        counter += 1
        if counter == 10:
            break

print(list)
