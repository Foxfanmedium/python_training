# class Country:
#
#     def __init__(self, population,main_nation, square_size ):
#         primary_question = str(input('Input your country:'))
#         self.population = population
#         self.nation = main_nation
#         self.square = square_size
#         print('Your country is:' + primary_question)
#
#     def dencity(self):
#         den = self.population/self.square
#         return den
#
# Germany = Country(500, 'Italian', 20000)
# print(Germany.nation)
# print(Germany.dencity())



class Human:
    def __init__(self, eyes, height, weight, nation):
        self.color_eyes = eyes
        self.height = height
        self.weight = weight
        self.nation = nation

    # @property
    # def nation(self):
    #     return self.nation

    def print_all(self):
        print('Your colour of eyes is:' + self.color_eyes)
        print('Your height is:' + str(self.height))
        print('Your weight is:' + str(self.weight))
        print('Your nation is:' + self.nation)
        # return print_all

Rail = Human('brown',180, 75, 'russian')
Rail.print_all()





