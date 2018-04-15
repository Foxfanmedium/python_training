# def min(*a):
#     m = a[0]
#     for x in a:
#         if m > x:
#             m = x
#     return m
#
#
# print(min(3,5))
# print(min(3, 6, 9, 8, 7, 0, 2, 6))
# =====================================================================================================================


def my_range(start, stop, step=1): # Precondition: start > stop if step > 0
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res


print(my_range(5, 25, 5))
