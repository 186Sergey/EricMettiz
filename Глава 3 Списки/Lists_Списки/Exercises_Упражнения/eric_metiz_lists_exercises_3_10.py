"""
Упражнение 3-10

Все функции.
Придумать информацию, которую можно было бы хранить в списке.
Например, список гор, городов, рек, стран, языков и др.
Написать программу, которая создаёт список элементов, а затем вызывает каждую функцию, упоминавшуюся
в этой главе, хотя бы один раз.
Функции, которые расматривались в этой главе:
    обращение к элементам списка по индексу
    использование отдельных элементов списка
    изменение элементов списка
    присоединение элементов в конец списка
    вставка элементов в список
    удаление элемента с использованием команды del
    удаление элемента с использованием метода pop()
    извлечение элементов из произвольной позиции списка
    удаление элементов по значению
    постоянная сортировка списка методом sort()
    временная сортировка списка функцией sorted()
    вывод списка в обратном порядке
    определение длины списка
"""

# список стран
countries = ['россия', 'франция', 'германия', 'англия', 'испания']
print(countries)
# список городов
cities = ['москва', 'париж', 'берлин', 'лондон', 'мадрид']
print(cities)
# список гор
mountains = ['кавказ', 'гималаи', 'карпаты', 'апенины', 'большой каньон']
print(mountains)
# список языков
languages = ['русский', 'францизский', 'немецкий', 'английский', 'испанский']
print(languages)
# список имён
names = ['николай', 'жан', 'ганс', 'конон', 'мигель']
print(names)
print("\n")

# Обращение к элементам списка по индексу
print("Обращение к элементам списка по индексу: ", countries[0].title(), countries[2].title(), countries[4].title())
print("Обращение к элементам списка по индексу: ", cities[0].title(), cities[1].title(), cities[3].title())
print("Обращение к элементам списка по индексу: ", mountains[0].title(), mountains[2].title(), mountains[3].title())
print("Обращение к элементам списка по индексу: ", languages[0], languages[4], languages[-2])
print("Обращение к элементам списка по индексу: ", names[0].title(), names[-3].title(), names[4].title())
print('\n')
# Использование отдельных элементов списка

print("Использование отдельных элементов списка: ", "Моя страна " + countries[0].title() + ", самая большая в мире.")
print("Использование отдельных элементов списка: ", "Столица моей родины - " + cities[0].title() + ".")
print("Использование отдельных элементов списка: ", "Самые красивые горы в нашей стране - " + mountains[0].title())
print("Использование отдельных элементов списка: ", "В школе я учил " + languages[2] + " язык.")
print("Использование отдельных элементов списка: ", "У меня взрослый сын, " + names[0].title() + ".")
print("\n")

# Присоединение элементов в конец списка с помощью метода append()
countries.append('греция')
print("Присоединение элементов в конец списка с помощью метода append():", countries)
cities.append('афины')
print("Присоединение элементов в конец списка с помощью метода append():", cities)
mountains.append('олимп')
print("Присоединение элементов в конец списка с помощью метода append():", mountains)
languages.append('греческий')
print("Присоединение элементов в конец списка с помощью метода append():", languages)
names.append('николас')
print("Присоединение элементов в конец списка с помощью метода append():", names)
print("\n")

# Вставка элементов в список при помощи метода insert()
countries.insert(3, 'колумбия')
print("Вставка элементов в список при помощи метода insert() ", countries)
cities.insert(5, 'богота')
print("Вставка элементов в список при помощи метода insert() ", cities)
mountains.insert(2, 'анды')
print("Вставка элементов в список при помощи метода insert() ", mountains)
languages.insert(1, 'португальский')
print("Вставка элементов в список при помощи метода insert() ", languages)
names.insert(4, 'фернандо')
print("Вставка элементов в список при помощи метода insert() ", names)
print("\n")

# Удаление элемента с использованием команды del
del countries[3]
print("Удаление элемента с использованием команды del: ", countries)
del cities[5]
print("Удаление элемента с использованием команды del: ", cities)
del mountains[1]
print("Удаление элемента с использованием команды del: ", mountains)
del languages[1]
print("Удаление элемента с использованием команды del: ", languages)
del names[4]
print("Удаление элемента с использованием команды del: ", names)
print("\n")

# Удаление элемента с использованием метода pop()
country = countries.pop()
print("Удаление элемента с использованием метода pop().", "Удалено: " + country.title(), countries)
city = cities.pop()
print("Удаление элемента с использованием метода pop().", "Удалено: " + city.title(), cities)
mountain = mountains.pop()
print("Удаление элемента с использованием метода pop().", "Удалено: " + mountain.title(), mountains)
language = languages.pop()
print("Удаление элемента с использованием метода pop().", "Удалено: " + language, languages)
name = names.pop()
print("Удаление элемента с использованием метода pop().", "Удалено: " + name.title(), names)
print("\n")

# Извлечение элементов из произвольной позиции списка
country = countries.pop(4)
print("Извлечение элементов из произвольной позиции списка с использованием метода pop().", "Удалено: "
      + country.title(), countries)
city = cities.pop(4)
print("Извлечение элементов из произвольной позиции списка с использованием метода pop().", "Удалено: "
      + city.title(), cities)
mountain = mountains.pop(4)
print("Извлечение элементов из произвольной позиции списка с использованием метода pop().", "Удалено: "
      + mountain.title(), mountains)
language = languages.pop(4)
print("Извлечение элементов из произвольной позиции списка с использованием метода pop().", "Удалено: "
      + language, languages)
name = names.pop(4)
print("Извлечение элементов из произвольной позиции списка с использованием метода pop().", "Удалено: "
      + name.title(), names)
print("\n")

# Удаление элементов по значению
countries.remove('англия')
print("Удаление элементов по значению с помощью метода remove(): ", countries)
cities.remove('лондон')
print("Удаление элементов по значению с помощью метода remove(): ", cities)
mountains.remove('апенины')
print("Удаление элементов по значению с помощью метода remove(): ", mountains)
languages.remove('английский')
print("Удаление элементов по значению с помощью метода remove(): ", languages)
names.remove('конон')
print("Удаление элементов по значению с помощью метода remove(): ", names)
print("\n")

# Присоединение элементов в конец списка с помощью метода append()
countries.append('греция')
print("Присоединение элементов в конец списка с помощью метода append():", countries)
cities.append('афины')
print("Присоединение элементов в конец списка с помощью метода append():", cities)
mountains.append('олимп')
print("Присоединение элементов в конец списка с помощью метода append():", mountains)
languages.append('греческий')
print("Присоединение элементов в конец списка с помощью метода append():", languages)
names.append('николас')
print("Присоединение элементов в конец списка с помощью метода append():", names)
print("\n")

# Вставка элементов в список при помощи метода insert()
countries.insert(3, 'колумбия')
print("Вставка элементов в список при помощи метода insert() ", countries)
cities.insert(5, 'богота')
print("Вставка элементов в список при помощи метода insert() ", cities)
mountains.insert(2, 'анды')
print("Вставка элементов в список при помощи метода insert() ", mountains)
languages.insert(1, 'португальский')
print("Вставка элементов в список при помощи метода insert() ", languages)
names.insert(4, 'фернандо')
print("Вставка элементов в список при помощи метода insert() ", names)
print("\n")

# Постоянная сортировка списка методом sort()
new_countries = countries[:]
new_cities = cities[:]
new_mountains = mountains[:]
new_languages = languages[:]
new_names = names[:]
print("Постоянная сортировка списка методом sort()", countries)
new_countries.sort()
print("Отсортированный список (копия): ", new_countries)
print("Постоянная сортировка списка методом sort()", cities)
new_cities.sort()
print("Отсортированный список (копия): ", new_cities)
print("Постоянная сортировка списка методом sort()", mountains)
new_mountains.sort()
print("Отсортированный список (копия): ", new_mountains)
print("Постоянная сортировка списка методом sort()", languages)
new_languages.sort()
print("Отсортированный список (копия): ", new_languages)
print("Постоянная сортировка списка методом sort()", names)
new_names.sort()
print("Отсортированный список (копия): ", new_names)
print("\n")

# Временная сортировка списка функцией sorted()
print("Список до сортировки: ", countries)
sorted(countries)
print("Временная сортировка списка функцией sorted(): ", new_countries)

print("Список до сортировки: ", cities)
sorted(cities)
print("Временная сортировка списка функцией sorted(): ", new_cities)

print("Список до сортировки: ", mountains)
sorted(mountains)
print("Временная сортировка списка функцией sorted(): ", new_mountains)

print("Список до сортировки: ", languages)
sorted(languages)
print("Временная сортировка списка функцией sorted(): ", new_languages)

print("Список до сортировки: ", names)
sorted(names)
print("Временная сортировка списка функцией sorted(): ", new_names)
print("\n")

# Вывод списка в обратном порядке
print(new_countries)
new_countries.sort(reverse=True)
print("Вывод списка в обратном порядке", new_countries)

print(new_cities)
new_cities.sort(reverse=True)
print("Вывод списка в обратном порядке", new_cities)

print(new_mountains)
new_mountains.sort(reverse=True)
print("Вывод списка в обратном порядке", new_mountains)

print(new_languages)
new_languages.sort(reverse=True)
print("Вывод списка в обратном порядке", new_languages)

print(new_names)
new_names.sort(reverse=True)
print("Вывод списка в обратном порядке", new_names)
print("\n")

# определение длины списка

countries.insert(3, 'алжир')
countries.insert(1, 'нигер')
countries.insert(4, 'турция')
print(countries)
cities.append('воронеж')
cities.pop()
print(cities)
mountains.pop()
print(mountains)
languages.append('китайский')
languages.append('бразильский')
languages.append('вьетнамский')
print(languages)
names.append('василий')
names.append('георгий')
names.pop(4)
print(names)

print("Длина списка равна: " + str(len(countries)) + " элементов.")
print("Длина списка равна: " + str(len(cities)) + " элементов.")
print("Длина списка равна: " + str(len(mountains)) + " элементов.")
print("Длина списка равна: " + str(len(languages)) + " элементов.")
print("Длина списка равна: " + str(len(names)) + " элементов.")
