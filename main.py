#class Dog

#опис класу, шаблон

class Dog:
    name = 'Monty'
    age = 2
    weight = 5

#можливість гавкати

    def make_sound(self):
        print('ГАВ')


  #конкретні песики

dog1 = Dog()

print(dog1.name)
print(dog1.age)
print(dog1.weight)

dog2 = Dog()

dog2.name = 'Lev'
print(dog2.name)
print(dog2.age)
print(dog2.weight)


#викристання метода
dog1.make_sound()