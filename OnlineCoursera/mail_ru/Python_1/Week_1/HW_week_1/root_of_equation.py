# Command Line Windows - >>> python
# a*(x**2) + b*x  + c = 0

#Version_1 via function gets_root(a,b,c)

import sys
from math import sqrt


def gets_roots(a, b, c):
    if a ==0:
        return None, None
    else:
        discriminant = b ** 2 - (4 * a * c)
        if discriminant > 0:
            print((-b - sqrt(discriminant))/2*a)
            print((-b + sqrt(discriminant))/2*a)
        elif discriminant == 0:
            print('x1 = x2 = ', -b / 2*a)
        else:
            return None, None


gets_roots(1, -3, -4)

#======================================================================================================================
#Version_2 via command line
# Command Line Windows - >>> python
# import sys
# from math import sqrt

# a = int(sys.argv[1])
# b = int(sys.argv[2])
# c = int(sys.argv[3])

# discriminant = (b ** b) - (4 * a * c)
# if discriminant > 0:
#     print((-b - sqrt(discriminant))/2*a)
#     print((-b + sqrt(discriminant))/2*a)
# elif discriminant == 0:
#     print('x1 = x2 = ', -b / 2*a)
# else:
#     print(discriminant)
#     print('too difficult')