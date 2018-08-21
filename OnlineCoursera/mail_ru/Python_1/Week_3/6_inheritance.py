class Pet:
    def __init__(self, name = None):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed = None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)
#
# dog = Dog("Шарик", "Доберман")
# print(dog.name)
# print(dog.say())


import json


class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name":self.name,
            "breed":self.breed
        })


class ExDog(Dog, ExportJSON):
    pass

dog = ExDog("Белка", breed = "Дворняжка")


print(dog.to_json())

print(ExDog.__mro__)








