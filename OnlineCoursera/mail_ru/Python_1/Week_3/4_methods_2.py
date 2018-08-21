# Статический метод класса


# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def is_age_valid(age):
#         return 0 < age < 150
#
# # Обращаться можно от имени класса
# print(Human.is_age_valid(35))  # -> True
# # Обращаться можно от экземпляра
# human = Human("Old Bobby")
#
# print(human.is_age_valid(234))  # -> False
#===========================================================================

# class Robot:
#
#     def __init__(self, power):
#         self.power = power
#
#
# wall_e = Robot(100)
# wall_e.power = 200
# print(wall_e.power)  # -> 200


# class Robot:
#
#     def __init__(self, power):
#         self.power = power
#
#     def set_power(self, power):
#         if power < 0:
#             self.power = 0
#         else:
#             self.power = power
#
# wall_e = Robot(100)
# wall_e.set_power(-200)
# print(wall_e.power)  # -> 0


# class Robot:
#
#     def __init__(self, power):
#         self.power = power
#
#     power = property()
#
#     @power.setter
#     def power(self, value):
#         if value < 0:
#             self._power = 0
#         else:
#             self._power = value
#
#     @power.getter
#     def power(self):
#         return self._power
#
#     @power.deleter
#     def power(self):
#         print("make robot useless")
#         del self._power
#
#
# wall_e = Robot(100)
# wall_e.power = -20
# print(wall_e.power)
#
# del wall_e.power




