def factorial(n):
    # Функція для обчислення факторіала числа n
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def number_of_groups(n, k):
    # Використовуємо формулу сполучень без повторень
    return factorial(n) // (factorial(k) * factorial(n - k))

# Тестуємо функцію
n = 50  # кількість підписників
k = 7   # кількість переможців

result = number_of_groups(n, k)
print(result)  # Це виведе кількість можливих різних списків переможців