# num = 13
# print(isinstance(num, int))  # Проверка принядлежит ли Num классу int
# print(isinstance(num, float))


# class Human:
#     pass


# class Robot:
#     """Данный класс позволяет создавать роботов"""
#
#
# print(Robot)
# print(dir(Robot))


# class Planet:
#     pass


# planet = Planet()
# print(planet)

#
# solar_system = []
# for i in range(8):
#     planet = Planet()
#     solar_system.append(planet)
#
# print(solar_system)
#
# solar_system = {}
# for i in range(8):
#     planet = Planet()
#     solar_system[planet] = True
#
# print(solar_system)


# class Planet:
#     def __init__(self, name):
#         self.name = name
#
#
# earth = Planet('Earth')
# print(earth.name)
# print(earth)


# class Planet:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# earth = Planet('Earth')
# print(earth)


class Planet:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Planet {self.name}"


solar_system = []

planet_names = ["Mercury", "Venus", "Earth",
                "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)
print(solar_system)




