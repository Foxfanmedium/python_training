# import pandas as pd
# dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
#        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
#        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#        "population": [200.4, 143.5, 1252, 1357, 52.98] }
# brics = pd.DataFrame(dict)
# print(brics)
# brics.index = ["BR", "RU", "IN", "CH", "SA"]
# print(brics)
#======================================================================================================================
# #if you have anv file with date about cars
# cars = pd.read_csv('cars.csv')
# print(cars)
#======================================================================================================================
import random
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))



