
"""
Упражнение 5-2

Больше условий. Количество условий не ограничивается 10. Программа должна выдавать по крайней мере один истинный или
один ложный результат для следующих
видов проверок.
    Проверка равенства и неравенства строк.
    Проверки с использованием функции lower().
    Числовые проверки равенства и неравенства, условий "больше", "меньше", "больше или равно", "меньше или равно".
    Проверки с ключевым словом and и or.
    Проверка вхождения элемента в список.
    Проверка отсутствия элемента в списке.
"""

strong = "Я изучаю Python"
string = "Мне нравится C#"

if len(strong) == len(string):
    print("Строки равны:", len(strong), len(string))
else:
    print("Строки не равны:", len(strong), len(string))

print("=" * 50)

car = 'Audi'
print(car)
print(car == 'audi')
print(car.lower() == 'audi')

print("!" * 50)
age = 45
print(age)

if age < 54:
    print("Меньше", age)
if age > 54:
    print("Больше", age)
if age <= 54:
    print("Меньше или равно", age)
if age >= 54:
    print("Больше или равно", age)

print("=" * 50)

temp = 21

if temp < 25 and temp < 22:
    print(True)
else:
    print(False)

temp2 = 21

if temp2 > 25 or temp2 < 20:
    print(True)
else:
    print(False)
print("*" * 50)

my_list = ['marine', 'elena', 'sergey', 'nikolay']

if 'sergey' in my_list:
    print("Такой есть")
else:
    print("Такого нет")

print('.' * 50)

banned_list = ['elena', 'sergey', 'bob']
user = 'tony'

if user not in banned_list:
    print("Добро пожаловать " + user.title())
else:
    print("Вы нарушили правила, " + user.title())
