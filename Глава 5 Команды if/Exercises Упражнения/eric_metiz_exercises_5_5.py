"""
Упражнение 5-5

Цвета

Преобразовать цепочку if-else из упражнения 5-4 в цепочку if-elif-else.
    если переменная содержит значение 'green', вывести сообщение о том, что игрок заработал 5 очков
    если переменная содержит значение 'yellow', вывести сообщение о том, что игрок заработал 10 очков
    если переменная содержит значение 'red', вывести сообщение о том, что игрок заработал 15 очков
    Написать три версии программы и проследить за тем, чтобы для каждого цвета пришелца выводилось соответствующее
    сообщение.
"""

alien_color = 'green'

if 'green' in alien_color:
    print("Вы заработали 5 очков!")
elif 'yellow' in alien_color:
    print("Вы заработали 10 очков!")
else:
    print("Вы заработали 15 очков!")

alien_color = 'yellow'

if 'green' in alien_color:
    print("Вы заработали 5 очков!")
elif 'yellow' in alien_color:
    print("Вы заработали 10 очков!")
else:
    print("Вы заработали 15 очков!")

alien_color = 'red'

if 'green' in alien_color:
    print("Вы заработали 5 очков!")
elif 'yellow' in alien_color:
    print("Вы заработали 10 очков!")
else:
    print("Вы заработали 15 очков!")

alien_color = 'green'

if alien_color == 'green':
    print("Вы заработали 5 очков!")
elif alien_color == 'yellow':
    print("Вы заработали 10 очков!")
else:
    print("Вы заработали 15 очков!")

alien_color = 'yellow'

if alien_color == 'green':
    print("Вы заработали 5 очков!")
elif alien_color == 'yellow':
    print("Вы заработали 10 очков!")
else:
    print("Вы заработали 15 очков!")

alien_color = 'red'

if alien_color == 'green':
    print("Вы заработали 5 очков!")
elif alien_color == 'yellow':
    print("Вы заработали 10 очков!")
else:
    print("Вы заработали 15 очков!")
