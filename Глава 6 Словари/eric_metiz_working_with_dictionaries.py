
"""
Работа со словарями.
Словарь в языке Python представляет собой совокупность пар "ключ-значение". Каждый ключ связывается с некоторым
значением, и программа может получить значение, связанное с данным ключом. Значением может быть число, строка, список
и даже другой словарь. Собственно, любой объект, создаваемый в программе Python, может стать значением в словаре.
В Python словарь заключается в фигурные скобки {}, в которых приводится последовательность пар "ключ-значение", как в
предыдущем примере:
"""

alien_0 = {'color': 'green', 'points': 5}

"""
ПАРА "КЛЮЧ-ЗНАЧЕНИЕ" представляет собой данные, связанные друг с другом. Если указать ключ, то Python вернёт значение, 
связанное с этим ключом. Ключ отделяется от значения двоеточием, а отдельные пары разделяются запятыми. В словаре 
может храниться любое количество пар "ключ-значение".
Простейший словарь содержит ровно одну пару "ключ-значение", как в следующей изменённой версии словаря alien_0:

alien_0 = {'color': 'green'}

В этом словаре хранится ровно один фрагмент информации о пришельце alien_0, а именно - его цвет. Строка 'color' 
является ключом в словаре. С этим ключом связано значение 'green'.
"""