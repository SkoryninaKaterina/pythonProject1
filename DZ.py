# import math
#
#
# def calculate_water_temperature(T_env, T0, t, k=0.05):
#
#     return T_env + (T0 - T_env) * math.exp(-k * t)
#
#
# T_env = 4  # Температура холодильника (в °C)
# T0 = 25  # Початкова температура води (в °C)
# t = 300  # Час у секундах
# k = 0.05  # Коефіцієнт охолодження
#
# result = calculate_water_temperature(T_env, T0, t, k)
# print(f"Температура води через {t} секунд: {result:.2f}°C")


# import time
#
#
# def get_name(show_time=False):
#     start_time = time.time()  # Початок вимірювання часу
#     name = input("Введіть своє ім'я: ")  # Запитуємо ім'я користувача
#     end_time = time.time()  # Кінець вимірювання часу
#
#     if show_time:
#         elapsed_time = end_time - start_time  # Розраховуємо час роботи функції
#         print(f"Час виконання функції: {elapsed_time:.2f} секунд")
#
#     return name  # Повертаємо ім'я
#
#
# user_name = get_name(show_time=True)
# print(f"Ваше ім'я: {user_name}")


from date_utils import days_until_deadline

def main():
    # Запитуємо дату дедлайну у користувача
    deadline = input("Введіть дату дедлайну у форматі YYYY-MM-DD: ")

    try:
        days_left = days_until_deadline(deadline)
        if days_left > 7:
            print(f"До дедлайну залишилося {days_left} днів.")
        elif days_left > 0:
            print(f"До дедлайну залишилося {days_left} днів. Поспішайте, залишилося менше тижня!")
        elif days_left == 0:
            print("Дедлайн сьогодні!")
        else:
            print("Дедлайн вже пройшов!")
    except ValueError as e:
        print(f"Помилка: {e}")

# Запуск програми
if __name__ == "__main__":
    main()

