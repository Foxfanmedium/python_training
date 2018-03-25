def double(arg):
    print('Before: ', arg)
    arg = arg *2
    print('After: ', arg)


double(5)


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)

change(['1', '2','3'])