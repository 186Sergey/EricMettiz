"""
Глава 6
Словари
В этой главе речь пойдёт о словарях - структурах данных, предназначенных для объединения взаимосвязанной
информации. Как получить доступ к информации, хранящейся в словаре, и как изменить эту информацию. Так как объём
данных в словаре практически безграничен, рассмотрим средства перебора данных в словарях. Кроме того, научимся
использовать вложенные словари в списках, вложенные списки в словарях и даже словари в других словарях.
Операции со словарями позволяют моделировать всевозможные реальные объекты с большей точностью. Вы узнаете, как создать
словарь, описывающий человека, и сохранить в нём сколько угодно информации об этом человеке. В словаре может
храниться имя, возраст, место жительства, профессия и любые другие атрибуты. Вы узнаете, как сохранить любые бва вида
информации, способные образовать пары - список слов и их значений, список имён людей и их любимых чисел, список гор и
их высот и т.д.
Простой словарь.
Возьмём игру с инопланетными пришельцами, которые имеют разные цвета и приносят разное количество очков игроку. В
следующем простом словаре хранится информация об одном конкретном пришельце:
"""

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

"""
В словаре alien_0 хранится два атрибута: цвет (color) и количество очков (points). Следующие две команды print() 
читают информацию из словаря и выводят её на экран.
Работа со словарями, как и большинство других новых концепций, требуют определённого опыта. Стоит немного поработать 
со словарями, и будет видно, как эффективно они работают при моделировании реальных ситуаций.
"""
