
"""
Упражнене 2-7

Удаление пропусков: сохранить имя пользователя в переменной. Добавить в начале и в конце имени несколько пропусков.
Проследить за тем, чтобы каждая служебная последовательность, "\t" и "\n", встречались по крайней мере один раз.

Вывести имя, чтобы были видны пропуски в начале и конце строки. Затем вывести его снова с использованием каждой из \
функций удаления пропусков: lstrip(), rstrip() и strip().
"""

famous_person = 'Сергей'
famous_person_left = '\tСергей'
famous_person_right = '\nСергей\t'
famous_person_split = '\t\tСергей\n\t'

print(famous_person)
print(famous_person_left)
print(famous_person_right)
print(famous_person_split)

print(famous_person_left.lstrip())
print(famous_person_right.rstrip())
print(famous_person_split.strip())
