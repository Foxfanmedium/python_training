# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


# class TownCar:
#
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#         print('Максимальная скорость машины:', speed)
#         print('У вас машина цвета', color)
#         print('У вас машина марки', name)
#         print('Полицейского ли типа у вас машина:', is_police)
#
#     def go(self, speed):
#         self.speed = speed
#         print('Вы едите со скоростью', speed, 'км/ч')
#
#     def stop(self):
#         print('Остановка на светофоре')
#
#     def turn(self, direction):
#         print('Поворот на', direction)
#
#
# class SportCar:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#         print('Максимальная скорость машины:', speed)
#         print('У вас машина цвета', color)
#         print('У вас машина марки', name)
#         print('Полицейского ли типа у вас машина:', is_police)
#
#     def go(self, speed):
#         self.speed = speed
#         print('Вы едите со скоростью', speed, 'км/ч')
#
#     def stop(self):
#         print('Остановка на светофоре')
#
#     def turn(self, direction):
#         print('Поворот на', direction)
#
#
# class WorkCar:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#         print('Максимальная скорость машины:', speed)
#         print('У вас машина цвета', color)
#         print('У вас машина марки', name)
#         print('Полицейского ли типа у вас машина:', is_police)
#
#     def go(self, speed):
#         self.speed = speed
#         print('Вы едите со скоростью', speed, 'км/ч')
#
#     def stop(self):
#         print('Остановка на светофоре')
#
#     def turn(self, direction):
#         print('Поворот на', direction)
#
#
# class PoliceCar:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#         print('Максимальная скорость машины:', speed)
#         print('У вас машина цвета', color)
#         print('У вас машина марки', name)
#         print('Полицейского ли типа у вас машина:', is_police)
#
#     def go(self, speed):
#         self.speed = speed
#         print('Вы едите со скоростью', speed, 'км/ч')
#
#     def stop(self):
#         print('Остановка на светофоре')
#
#     def turn(self, direction):
#         print('Поворот на', direction)
#
#
# my_car = TownCar(250, 'red', 'mazda', False)
# # print(my_car.go(90))
# # print(my_car.stop())
# # print(my_car.turn('Право'))
# print('================================')
# mercedes = SportCar(320, 'white', 'mercedes', False)
# # print(my_car.go(90))
# # print(my_car.stop())
# # print(my_car.turn('Право'))
# print('================================')
# wolkswagen = WorkCar(180, 'black', 'wolkswagen', False)
# # print(my_car.go(90))
# # print(my_car.stop())
# # print(my_car.turn('Право'))
# print('================================')
# wolkswagen = PoliceCar(280, 'white-black', 'porshe', True)
# # print(my_car.go(90))
# # print(my_car.stop())
# # print(my_car.turn('Право'))
# print('================================')

# Решение преподавателя
#
# class TownCar:
#
#     def __init__(self, speed, color,name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print('{} is going!'.format(self.name))
#
#     def stop(self):
#         print('{} is stopping!'.format(self.name))
#
#     def turn(self, direction):
#         print('{} is turning to {}'.format(self.name, direction))
#
#
# class SportCar:
#     def __init__(self, speed, color, name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print('{} is going!'.format(self.name))
#
#     def stop(self):
#         print('{} is stopping!'.format(self.name))
#
#     def turn(self, direction):
#         print('{} is turning to {}'.format(self.name, direction))
#
#
# class WorkCar:
#     def __init__(self, speed, color, name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print('{} is going!'.format(self.name))
#
#     def stop(self):
#         print('{} is stopping!'.format(self.name))
#
#     def turn(self, direction):
#         print('{} is turning to {}'.format(self.name, direction))
#
#
# class PoliceCar:
#     def __init__(self, speed, color, name, is_police=True):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print('{} is going!'.format(self.name))
#
#     def stop(self):
#         print('{} is stopping!'.format(self.name))
#
#     def turn(self, direction):
#         print('{} is turning to {}'.format(self.name, direction))

#======================================================================================================================

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


# class BaseCar:           # Выносим общие атрибуты отдельно. Далее делаем наследование для каждого класса
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#         print('Максимальная скорость машины:', speed,)
#         print('У вас машина цвета', color)
#         print('У вас машина марки', name)
#         print('Полицейского ли типа у вас машина:', is_police)
#
#
# class TownCar(BaseCar):
#
#     def go(self, speed):
#         self.speed = speed
#         print('Вы едите со скоростью', speed, 'км/ч')
#
#     def stop(self):
#         print('Остановка на светофоре')
#
#     def turn(self, direction):
#         print('Поворот на', direction)
#
#
# class SportCar(BaseCar):
#
#     def go(self, speed):
#         self.speed = speed
#         print('Вы едите со скоростью', speed, 'км/ч')
#
#     def stop(self):
#         print('Остановка на светофоре')
#
#     def turn(self, direction):
#         print('Поворот на', direction)
#
#
# class WorkCar(BaseCar):
#
#     def go(self, speed):
#         self.speed = speed
#         print('Вы едите со скоростью', speed, 'км/ч')
#
#     def stop(self):
#         print('Остановка на светофоре')
#
#     def turn(self, direction):
#         print('Поворот на', direction)
#
#
# class PoliceCar(BaseCar):
#
#     def go(self, speed):
#         self.speed = speed
#         print('Вы едите со скоростью', speed, 'км/ч')
#
#     def stop(self):
#         print('Остановка на светофоре')
#
#     def turn(self, direction):
#         print('Поворот на', direction)

# Решение преподавателя


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('{} is going'.format(self.name))

    def stop(self):
        print('{} is stopping'.format(self.name))

    def turn(self,direction):
        print('{} is turning to {}'.format(self.name, direction))


class TownCar(Car):
    pass


class SportCar(Car):
    def __init__(self, speed, color, name, has_turbo = True):
        super().__init__(speed, color, name)
        self.has_turbo = True


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


sportCar = SportCar(240, 'Red', 'Sport Car')
townCar = TownCar(140, 'Grey', 'Town Car')
workCar = WorkCar(90, 'Yellow', 'Work Car')
policeCar = PoliceCar(210, 'Blue', 'Police Car')

print(policeCar.is_police)

























