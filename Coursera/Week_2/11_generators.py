# def even_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 2
#
# # print(list(even_range(2, 21)))
# ranger = even_range(0, 4)
# next(ranger)
#=====================================================================================================================
# def list_generator(list_obj):
#     for item in list_obj:
#         yield item
#         print('After yielding {}'.format(item))
#
# generator = list_generator([1,2])
#
# print(next(generator))
#=====================================================================================================================
# def fibonacci(number):
#     a = b = 1
#     for _ in range(number):
#         yield a
#         a, b = b, a +b
#
# print(list(fibonacci(20)))
#=====================================================================================================================
def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value:break
        total += value

generator = accumulator()

print(list(generator))
print('Accumulated: {}'.format(generator.send(1)))






