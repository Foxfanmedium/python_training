# def even_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current +=2
#
# for number in even_range(1, 16):
#     print(number)


# def list_generator(list_obj):
#     for item in list_obj:
#         yield item
#         print('After yielding {}'.format(item))
# generator = list_generator([1, 8])
#
# print(next(generator))


# def fibonacci(number):
#     a = b = 1
#     for _ in range(number):
#         yield a
#         a, b = b, a + b
#
# for num in fibonacci(15):
#     print(num)

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end='\n')
        a, b = b, a+b
    print()

fibonacci(2000)




def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value:break
        total += value

generator = accumulator()
















