
"""
Сравнения чисел.

Проверка числовых значений достаточно прямолинейна. Например, переменная age равна 18:
"""

age = 10

if age != 18:
    print(False)

"""
Также можно проверить условие неравенства двух чисел. Например, если значение переменной answer отлично от 
ожидаемого:
"""

answer = 17
if answer != 42:
    print("Это неверный ответ. Пожалуйста, попробуйте еще раз!")

"""
В условные команды также можно включать всевозможные матаматические сравнения: меньше <, меньше или равно <=, 
больше >, больше или равно >=:
"""

age = 20

if age < 18:
    print("Чуть чуть подрасти!")

if age <= 17:
    print("Тебе сюда рано!")

if age > 19:
    print("Добро пожаловать")

if age >= 18:
    print("Теперь и тебе можно")

"""
Все математические сравнения могут использоваться в условиях if, что повышает точность формулировки интересующих 
условий.
"""
