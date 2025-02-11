# #class Dog
#
# #опис класу, шаблон
from tkinter.font import names


# class Dog:
#
# #конструкто для створення обектів класу
#     def __init__(self,name,age,weight):
#         if age < 0:
#             raise ValueError('вік пса не може бути відемним')
#
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#
# # можливість гавкати
#
#     def make_sound(self):
#         print('ГАВ')
#
#     def print_info(self):
#         print(self.name, self.age, self.weight)
#
#     def rename(self,new_name):
#         #зміна імені песика
#         self.name = new_name
#   #конкретні песики
# #
# # # dog1 = Dog()
# # #
# # # print(dog1.name)
# # # print(dog1.age)
# # # print(dog1.weight)
# # #
# # # dog2 = Dog()
# # #
# # # dog2.name = 'Lev'
# # # print(dog2.name)
# # # print(dog2.age)
# # # print(dog2.weight)
# # #
# # #
# # # #викристання метода
# # # dog1.make_sound()
# #
# # dog1 = Dog(name='lev', age=3,weight=5)
# # print(dog1.name)
# #
# # dog2 = Dog(name='Carl', age=3,weight=5)
# # print(dog2.name)
# #
# # dog1.print_info()
# # dog2.print_info()
#
# dog = Dog(name='Carl', age=3,weight=5)
# dog.print_info()
#
# dog.rename('петро')


# Завдання 1
# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік:
# {age}»

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Імя: {self.name}")
        print(f"Вік: {self.age}")
        print()


# student1 = Student('Stiv', 22)
# student2 = Student("Victor", 38)
# student3 = Student("Victoriia", 35)
#
# student1.print_info()
# student2.print_info()
# student1.print_info()
# student3.print_info()


# Завдання 2
# Створіть список з 3-ма студентами, дані вводить
# користувач. Після чого для кожного студента виведіть
# інформацію про нього за допомогою метода.

students = []

for _ in range(3):
    name = input('імя ')
    age = int(input('Вік '))

    student=Student(name, age)
    students.append(student)


for student in students:
    student.print_info()

