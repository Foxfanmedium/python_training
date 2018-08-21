class Car:
    def __init__(self, colour, age, mark):
        self.colour = colour
        self.age = age
        self.mark = mark

    def price_depend_age(self):
        # self.age = age
        if self.age > 10:
            print('To old car')
        else:
            print('Your price will be nice')


bently = Car('Yeelow', 15, 'Bently')

print(bently.price_depend_age())
