# #class Dog
#
# #опис класу, шаблон

class Dog:

#конструкто для створення обектів класу
    def __init__(self,name,age,weight):
        if age < 0:
            raise ValueError('вік пса не може бути відемним')

        self.name = name
        self.age = age
        self.weight = weight


# можливість гавкати

    def make_sound(self):
        print('ГАВ')

    def print_info(self):
        print(self.name, self.age, self.weight)
  #конкретні песики

# dog1 = Dog()
#
# print(dog1.name)
# print(dog1.age)
# print(dog1.weight)
#
# dog2 = Dog()
#
# dog2.name = 'Lev'
# print(dog2.name)
# print(dog2.age)
# print(dog2.weight)
#
#
# #викристання метода
# dog1.make_sound()

dog1 = Dog(name='lev', age=3,weight=5)
print(dog1.name)

dog2 = Dog(name='Carl', age=3,weight=5)
print(dog2.name)

dog1.print_info()
dog2.print_info()