
"""
Упражнение 4-8
Кубы.
Создать список первых 10 кубов (то есть кубов всех целых чисел от 1 до 10) и вывести значения всех кубов в цикле for
"""

squares = list(range(1, 11))

for square in squares:
    value = square**3
    print("Сумма куба " + str(square) + ":", value)
