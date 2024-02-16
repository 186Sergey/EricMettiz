
"""
Выполнение действий после цикла for

Что происходит после завершения цикла for? Обычно программа выводит свободную информацию или
переходит к другим действиям.
Каждая строка кода после цикла for, не имеющая отступа, выполняется без повторения. Чтобы вывести общее сообщение
после всех отдельных сообщений, разместить надо после цикла for без отступов:
"""

# Вывод общего сообщения для всех после цикла for

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", это был отличный трюк!")
    print("Я не могу дождаться, когда увижу твой следующий трюк, " + magician.title() + ".\n")

print("Спасибо вам всем. Это было великолепное волшебное шоу!")
