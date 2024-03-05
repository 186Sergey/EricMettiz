"""
Упражнение 5-1
Проверка условий.
Написать последовательность условий. Вывести описание каждой проверки и прогноз относительно её результата. Код
должен выглядеть примерно так:
    car = 'subaru'
        print("Is car == 'subaru'? I predict True.")
        print(car == 'subaru')
        print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')
    Внимательно посмотрите результаты. Убедится в том, что вы понимаете, почему результат каждой строки равен True
    или False.
    Создать как минимум 10 условий. не менее 5 должны давать результат True, а не менее 5 других - результат False.
"""

a = 'bmw'
print(a == 'bmw')
print("Да, это " + a.title() + ".\n")

print(a == 'audi')
print("Нет, это " + a.title() + ".\n")

b = 'pepperoni'
c = 'pepper' == b
print(c)
print("Нет это " + b.title(), '\n')

car = 'audi'
print(car == 'audi')
print("Да, это " + car.title(), '\n')
