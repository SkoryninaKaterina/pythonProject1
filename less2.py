# # Завдання 1
# # Створіть клас Проект з атрибутами:
# #  назва
# #  виділений кошторис
# #  загальні витрати
# #  чи завершений(за замовчуванням False)
# #  час виконання(за замовчуванням 0 місяців)
# #  список необхідних задач
# # Додайте методи:
# #  вивід інформації: назва, час виконання, необхідні
# # задачі
# #  добавити нову задачу
# #  розбити задачу на під-задачі: передається назва задачі
# # та список під-задач
# #  виконати задачу, передається назва, час та ціна
# # виконання
# #  поповнення кошторису
# from distutils.sysconfig import project_base
#
#
# class Project:
#     def __init__(self, name, budget, tasks):
#         self.name = name
#         self.budget = budget
#         self.tasks = tasks
#
#         self.expenses = 0
#         self.is_finished = False
#         self.spent_time = 0  # місяці
#
#         if len(self.tasks) == 0:
#             self.is_finished = True
#
#
#     def display_info(self):
#         print(f'Проект{self.name}')
#         print(f"Час виконання {self.spent_time} місяців")
#         print(f'витравчено {self.expenses}/{self.budget}$')
#         print(f'залишилось {self.budget - self.expenses}$')
#
#         if self.is_finished:
#             print('стан проекту завершений')
#         else:
#             print('стан проекту незавершений')
#
#
#             print('задачі що залишились:')
#             for task in self.tasks:
#                 print(f'   - {task}')
#
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#
#     def divide_task(self, task, subtasks):
#         if task not in self.tasks:
#             print('немає такої задачі')
#             return
#
#
#
#
#         self.tasks.remove(task)
#
#         self.tasks += subtasks
#
#     def do_task(self, task, duration, price):
#         if task not in self.tasks:
#             print('немає такої задачі')
#             return
#
#         free_money = self.budget - self.expenses
#         if price > free_money:
#             print('недостатньо коштів')
#             return
#         self.expenses += price
#
#     def update_budget(self, amount):
#         self.budget += amount
#
# project = Project(name='Ігрушка',
#                   budget=10_000,
#                   tasks=['знайти інвесторів',
#                          "придумати загальну ідею"])
#
# project.display_info()
#
# project.add_task('Вибрати ПЗ для гри')
#
# project.display_info()
#
# project.divide_task('організувати бенкет',
#                     ['витратити бюджет'])
#
# project.divide_task('придумати загальну ідею',
#                     ['обрати між 2Д та 3Д'
#                      "придумати сюжет",
#                      "пропиати персонажів"])
#
# project.display_info()
#
#
# project.do_task('Придумати сюжет', 6, 1000)
# project.do_task('Обрати між 2D та 3D', 3, 200)
# project.do_task('Прописати персонажів', 15, 6000)
#
# project.update_budget(2500)
#
# project.do_task('Знайти інвесторів', 10, 3000)
# project.do_task('Вибрати ПЗ для гри', 5, 1800)
#
# project.display_info()


# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
# Практичне завдання
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ –
# назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон

class Phone:
    def __init__(self, max_memory, apps):
        self.max_memory = max_memory
        self.is_on = False
        self.apps = apps

        self.used_memory = 0 # рахуємо память
        for app_name in self.apps:
            self.used_memory += self.apps[app_name]

    def display_info(self):
        print(f'використана память {self.used_memory}/{self.max_memory}ГБ')
        print(f'встановлені додатки')
        for app_name in self.apps:
            print(f'встановлений додаток {app_name} -{self.apps [app_name]} ГБ')
        print()
        print()

    def delete_app(self, app_name):
        if app_name not in self.apps:
            print('немає такого додатку')
            return

        app_memory = self.apps.pop(app_name)
        self.used_memory -= app_memory

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

phone = Phone(128,
              {'Google': 30,
              'Ytube': 20,
               'Telegram':5})

phone.display_info()

phone.delete_app('Ytube')

phone.display_info()
