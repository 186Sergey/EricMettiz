"""
Упражнение 5-9
Без пользователей.
Добавить в команду if, которая проверит, что список пользователей не пуст.
    Если список пуст, вывести сообщение: "Нам нужно найти несколько пользователей!"
    Удалить из списка все имена пользователей и убедиться в том, что программа выводит сообщение правильно.
"""

user_names = ['marina', 'nikolai', 'dmitry', 'admin', 'elena', 'fedor', 'oksana']

if user_names:
    for user_name in user_names:
        print("Добро пожаловать на сайт " + str(user_name.title()) + "!")
else:
    print("Вы не зарегистрированы!")


user_names = []

if user_names:
    for user_name in user_names:
        print("Добро пожаловать на сайт " + str(user_name.title()) + "!")
else:
    print("\nВы не зарегистрированы!")
