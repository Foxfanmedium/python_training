# class Planet:
#
#     count = 0
#
#     def __init__(self, name, population=None):
#         self.name = name
#         self.population = population or []
#         Planet.count += 1
#
# earth = Planet('Earth')
# mars = Planet('Mars')
#
# print(Planet.count)


# class Human:
#
#     def __del__(self):  # деструктор дял удпаления экземпляра класса
#         print("Goodbye!")
#
# human = Human()
# del human


# class Planet:
#     """This class describes planets"""
#
#     count = 1
#
#     def __init__(self, name, population=None):
#         self.name = name
#         self.population = population or []


# planet = Planet('Earth')
# # print(planet.__dict__)
# planet.mass = 5.9e24
# # print(planet.__dict__)
# print(Planet.__dict__)
#
# print(Planet.__doc__)  # -> This class describes planets
# print(planet.__doc__)  # -> This class describes planets
#
# print(dir(planet))
# print(planet.__class__)  # -> <class '__main__.Planet'>


# Констрктор экземпляра класса
# class Planet:
#     def __new__ (cls, *args, **kwargs):
#         print("__new__ called")
#         obj = super().__new__(cls)
#         return obj
#
#     def __init__(self, name):
#         print("__init__ called")
#         self.name = name


# earth = Planet("Earth")  # -> __new__ called
#                          #__init__ called























