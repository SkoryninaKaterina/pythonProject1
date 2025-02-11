# функція як об'єкт в Python

# num = 10
# num2 = num
#
# my_print = print
#
# my_print(1, 2, 3, sep=', ')
# print(4, 5, 6, end='!\n')
#
#
# # print = 'hello'
# # print(1, 2, 3)
#
#
# def hello():
#     print('hello')
#
#
# hello = 'hello, world'
# hello()


# def mean(nums):
#     return sum(nums) / len(nums)
#
#
# nums = [1, 2, 3, 4]
# words = ['apple', 'banana']
#
#
# funcs = [sum, min, max, mean]
#
# #for num in nums:
# for func in funcs:
#     print(f"{func.name} -- {func(nums)}")

# є функція, яка визначає певну умову. Використовуючи її
# Дістати зі списку чисел ті числа які відповідають умові.

# def filter_with_condition(nums, condition):
#     new_nums = []
#
#     for num in nums:
#         if condition(num):
#             new_nums.append(num)
#
#     return new_nums
#
#
# def is_positive(num):
#     return num > 0
#
#
# def is_even(num):
#     return num % 2 == 0
#
#
# def is_zero(num):
#     return num == 0
#
#
# def new_func(num):
#     return is_even(num) or is_positive(num)
#
#
# nums = [1, 2, 0, 0, -2, -5, 8, 0, -7]
#
#
# result = filter_with_condition(nums, is_zero)
# print(result)
#
#
# for func in [is_even, is_positive, is_zero, new_func]:
#     result = filter_with_condition(nums, func)
#     print(result)

#
# def filter_with_condition(nums, condition):
#     new_nums = []
#
#     for num in nums:
#         if condition(num):
#             new_nums.append(num)
#
#     return new_nums
#
#
# def is_positive(num):
#     return num > 0
#
#
# def is_even(num):
#     return num % 2 == 0
#
#
# def is_zero(num):
#     return num == 0
#
#
# def new_func(num):
#     return is_even(num) or is_positive(num)
#
#
# nums = [1, 2, 0, 0, -2, -5, 8, 0, -7]
#
#
# result = filter_with_condition(nums, is_zero)
# print(result)
#
#
# for func in [is_even, is_positive, is_zero, new_func]:
#     result = filter_with_condition(nums, func)
#     print(result)
#
# # анонімні функції, lambda функції
# def is_positive(num):
#     return num > 0
#
#
# is_positive = lambda num: num > 0
#
# mult_2 = lambda num: 2*num
# print(mult_2(10))
#
# # дістати від'ємні числа зі списку
# result = filter_with_condition(nums,
#                                condition=lambda num: num < 0)
#
# print(result)
#
# # теж саме, але з filter
# result = filter(lambda num: num<0, nums)
# result = list(result)
# print(result)
#
# # число більше 10
# lambda num: num > 10
#
# # число трьохцифрове
# lambda num: 100 <= num <= 999
#
# # у слові є буква а
# lambda word: 'a' in word
#
# # додати 10 до числа
# lambda num: num + 10
#
# # перевести слово у lower
# lambda word: word.lower()
#
# # перевести слово у upper
# lambda word: word.upper()
#
#
# words = ['apple', 'kiwi', 'banana']
#
# words_a = filter(lambda word:'a' in word,
#                  words)
# words_a = list(words_a)
# print(words_a)


# # сортування
# nums = [1, 2, 0, 0, -2, -5, 8, 0, -7]
# words = ['apple', 'kiwi', 'banana']
#
# result = sorted(nums)
# print(result)
#
# result = sorted(words)  # за алфавітом
# print(result)
#
# # сортувати слова за довжиною
# result = sorted(words, key=lambda word: len(word))
# print(result)
#
# # сортувати за кількістю букв а
# result = sorted(words, key=lambda word: word.count('a'))
# print(result)
#
# # отримати найдовше слово
# result = max(words, key=lambda word: len(word))
# print(result)

# Завдання 1
# Напишіть lambda-функції, які:
#  Підносить число до квадрату
#  Отримує довжини трикутника і повертає периметр
#  Отримує прізвище та ім’я і повертає рядок у форматі
# «Прізвище, ім’я»
#  Перевіряє чи є число парним

# num = int(input('ведите число'))
#
# # key = lambda num: num**2
# # print(key(num))
#
# key = lambda num: num %2 ==0
# print(key(num))


# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел та повертає список з лише
# додатніми числами
#  Отримує список слів та повертає список слів, в яких
# більше ніж 3 літери
#  Отримує список слів та літеру і повертає список тих
# слів, які починаються на цю літеру(регістр
# неважливий)


# nums = [1, 2, -5, 6, -7]

# pozitiv_num = filter(lambda num: num > 0, nums)
#
# pozitiv_num = list(pozitiv_num)
# print(pozitiv_num)

# words = ['papaya', 'banana', 'nana', 'al', 'papaya']
# letter = 'p'

#
# fri_letters = filter(lambda word: len(word) > 3, words)
#
# fri_letters = list(fri_letters)
#
# print(fri_letters)

# lists = filter(lambda word: word[0] == letter, words)
#
# lists = list(lists)
#
# print(lists)

# Завдання 4
# Напишіть функції, які:
#  Сортує список слів за останньою літерою
#  Сортує список чисел за кількістю цифр
#  Знаходить число зі списку, яке найближче до
# заданого(передається як параметр)
#  Знаходить слово у списку з найменшою довжиною
#  Сортує список чисел за кількістю цифр, якщо кількість
# цифр однакова, то сортує за значенням числ

# words = ['papaya', 'banana', 'nana', 'al', 'papaya']
# list_new = sorted(words, key=lambda word: word[-1])
# print(list_new)

#  Сортує список чисел за кількістю цифр
# nums = [1, 2, -5, 6, 23, 164, 2, 0]
# new_nums = sorted(nums, key= lambda num: len(str(abs(num))))
# print(new_nums)

#  Знаходить слово у списку з найменшою довжиною
# words = ['papaya', 'banana', 'nana', 'al', 'papaya']
# min_word = min(words, key= lambda word: len(word))
# print(min_word)

#  Знаходить число зі списку, яке найближче до
# заданого(передається як параметр)

# nums = [1, 2, -5, 6, 23, 164, 2, 0]
# target = int(input("Введіть число: "))
# res = min(nums, key=lambda num: abs(num - target))
# print(res)


#  Отримує довжини трикутника і повертає периметр

# lambda a, b, c: a + b + c

# Є список людей(ім'я та прізвище), відсортувати за
# прізвищем, якщо прізвища однакові, сортувати за
# іменем.

# 'D John'
# ['D', 'John']


#people = [['D', 'John'],
          # ['A', 'Max'],
          # ['G', 'David'],
          # ['B', 'Shohn'],
          # ['A', 'Ann'],
          # ['A', 'John']]


# Відсортувати за прізвищем

# sorted_list = sorted(people, key=lambda person: person[0])
#
# for person in sorted_list:
#     print(person)

# # Відслртувати за іменем
# sorted_list = sorted(people, key=lambda person: person[1])
#
# for person in sorted_list:
#     print(person)

# Спочатку прізвище а потім за іменем

# print(10 > 5)
# print('apple' > 'banana')
# print([1, 3] > [1, 2])
#
# sorted_list = sorted(people, key=lambda person: [person[0], person[1]])
#
# for person in sorted_list:
#     print(person)

# Сортує список чисел за кількістю цифр, якщо кількість
# цифр однакова, то сортує за значенням числа


# nums = [1, 2, -5, 6, 23, -164, 2, 0]

# new_nums = sorted(nums, key=lambda num: [len(str(abs(num))), num])
# print(new_nums)






# Завдання 1
# Напишіть lambda-функції, які:
#  Множить число на -1
#  Перевіряє чи рядок непорожній

# minus_one = lambda x: x * -1
#
# result1 = minus_one(5)  # -5
# result2 = minus_one(-10)  # 10
# print(f"Результат множення: {result1}, {result2}")
#
#
# is_non_empty_string = lambda s: bool(s)
#
# result1 = is_non_empty_string("Hello")  # True
# result2 = is_non_empty_string("")  # False
# print(f"Рядок непорожній: {result1}, {result2}")
#
#
# Завдання 2
# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел, рахує середнє арифметичне та
# повертає список з числами, які більші за середнє
#  Отримує список слів та повертає список слів, в яких
# рівно 4 літери
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# filtered_numbers = list(filter(lambda x: x > (sum(numbers) / len(numbers)) if numbers else False, numbers))
#
#
# words = ["tree", "apple", "word", "bird", "cat"]
# filtered_words = list(filter(lambda word: len(word) == 4, words))
#
# print("Числа більші за середнє:", filtered_numbers)
# print("Слова з 4 літерами:", filtered_words)


# Завдання 3
# Напишіть функцію, яка отримує літеру та список слів і
# знаходить слово зі списку, в якому найбільша кількість даної
# літери.
#
# words = ["tree", "apple", "word", "bird", "cat"]
# letter = 'p'
# word_with_max_letter = max(words, key=lambda word: word.count(letter), default=None)
#
# print(f"Слово з найбільшою кількістю літери '{letter}





