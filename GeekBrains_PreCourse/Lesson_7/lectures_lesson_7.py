from itertools import chain
import itertools

# it1 = iter([1,2,3])
# it2 = iter([7,8,0])
#
# for i in chain(it1, it2):
#     print(i)
#
# for i in itertools.count(1):
#     print(i)
#     if i > 20:
#         break

# tango = [1,2,3]
# for i in itertools.cycle(tango):
#     print(i)


# for i in itertools.takewhile(lambda x: x > -10, [9, 5, -4, 7, 1, -2, 3, -5, 8, 0, 9]):
#     print(i)

# for i in itertools.dropwhile(lambda x: x > -3, [10, 8, 7, -2, 3, -3, 6, 0, 8, -3, 1, 2, -2, -7, 4, -3]):
#     print(i)

#
# class Fibonacchi:
#     def __init__(self, N):
#         self.n, self.a, self.b, self.max = 0, 0, 1, N
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             a, self.n, self.a, self.b = self.a, self.n + 1, self.b, self.a + self.b
#             return a
#         else:
#             raise StopIteration
#
#
# for i in Fibonacchi(10):
#     print(i)


# class A:
#     def go(self):
#         print('Go, A!')
#
#
# class B(A):
#     def go(self, name):
#         print('Go, {}!'.format(name))
#
#
# go_name = B()
# go_name.go('Ivan')


class Car:

    def __init__(self):
        self.modules = []

    def __str__(self):
        return str(self.modules)

    def __add__(self, other):
        self.modules.append(other)
        return self

    def add_module(self, module):        # лучше использовать создание нового метода чем переопределять метод __add__
        self.modules.append(module)


car = Car()
car = car + 'кондиционер'
car = car + 'усилитель руля'

car.add_module('подогрев руля')

print(car)
