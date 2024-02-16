
"""
Целые числа

В Pythonс целыми числами можно выполнять операции:
    сложения (+);
    вычитания (-);
    умножения (*);
    деления (/).
"""
addition = 2 + 3
subtraction = 5 - 3
multiplication = 5 * 3
division = 3 / 2

print('Сложение 2 + 3')
print(addition, '\n')
print('Вычитание 5 - 3')
print(subtraction, '\n')
print('Умножение 5 * 3')
print(multiplication, '\n')
print('Деление 3 / 2')
print(division)

"""
Для представления операции возведения в степень в Python используется сдвоенный знак умножения.
"""

print('Возведение в степень 3 ** 2')
degree = 3 ** 2
print(degree)

print('Возведение в степень 3 ** 3')
degree = 3 ** 3
print(degree)

print('Возведение в степень 10 ** 6')
degree = 10 ** 6
print(degree)

"""
В Python также существует определённый порядок операций, что позволяет использовать несколько операций в одном 
выражении. Круглые скобки используются для изменения порядка операций, чтобы выражение могло вычисляться в нужном 
порядке.
"""

addition_multiplication = 2 + 3*4
print('Выводим результат выражения 2 + 3*4')
print(addition_multiplication)

print('Выводим результат выражения (2 + 3)*4')
addition_multiplication_2 = (2 + 3) * 4
print(addition_multiplication_2)
