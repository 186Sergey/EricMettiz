
"""
Изменение, добавление и удаление элементов

Добавление элементов в список

Новые элементы могут добавляться в списки по разным причинам. Python предоставляет несколько способов добавления новых
данных в существующие списки.
    Присоединение элементов в конец списка.

Простейший способ добавления новых элементов в список - присоединение элемента в конец списка.
Метод append() присоединяет строку в конец списка, другие элементы в списке при этом остаются неизменными.
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('dukati')
print(motorcycles)

"""
Метод append() упрощает динамическое построение списков. Например, можно начать с пустого списка и добавлять в него 
элементы серией команд append().
"""

print('Создадим пустой список motorcycles. motorcycles = []')
motorcycles = []

print("Далее при помощи метода append(), добавим в список новые элементы - motorcycles.append('значение')")
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yamaha')
print("Выводим на экран результат")
print(motorcycles)

"""
Вставка элементов в список

Метод insert() позволяет добавить новый элемент в произвольную позицию списка. Для этого следует указать индекс и 
значение нового элемента.
Например:
    motorcycles.insert(0, 'dukati')
    где 0 - это индекс нового (вставляемого) элемента
        'dukati' - значение нового (вставляемого) элемента

Метод insert() выделяет свободное место в позиции, в которую вставляется новый элемент, и сохраняет в нём значение. 
Все остальные значения списка при этом сдвигаются на одну позицию вправо.
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print("Вставляем в список, при помощи метода insert(), новое значение 'dukati' в позицию с индексом 0")
motorcycles.insert(0, 'dukati')
print("Выводим результат на экран.")
print(motorcycles)
