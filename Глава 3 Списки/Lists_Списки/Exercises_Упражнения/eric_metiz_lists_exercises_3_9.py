
"""
Упражнение 3-9

Количество гостей.
Из упражнений с 3-4 по 3-7, используя функцию len(), посчитать количество гостей, приглащённых на обед.
"""

my_friends = ['николай', 'елена', 'дмитрий', 'владимир', 'марина']
print("Количество гостей в упражнении 3-4:", len(my_friends))


my_friends = ['николай', 'елена', 'дмитрий', 'владимир', 'марина']
print(my_friends)

remove_friend = my_friends.pop(0)
print("Дорогие друзья. К сожалению " + remove_friend.title() + " прийти не сможет.")
my_friends.insert(0, 'григорий')
print(my_friends)
print("Количество гостей в упражнении 3-5:", len(my_friends))


my_friends = ['николай', 'елена', 'дмитрий', 'владимир', 'марина']
print(my_friends)
print("Список с новыми гостями.")
new_friends = []
print(new_friends)
print("Добавим в список новых гостей при помощи методов insert() и append()")
new_friends.insert(0, 'олег')
new_friends.insert(1, 'оксана')
new_friends.append('наталья')
print(new_friends)

print("Объединение двух списков в один (new_list = my_friends.copy() + new_friends.copy())")
new_list = my_friends.copy() + new_friends.copy()
print(new_list)
print("Количество гостей в упражнении 3-6:", len(new_list))


guest_list = ['николай', 'марина', 'сергей', 'елена', 'фёдор']
print("На обед приглашаются только " + guest_list[-1].title() + " и " + guest_list[1].title() + ".")

guest_it_remains = []

guest_remains = guest_list.pop(-2)
guest_it_remains.append(guest_remains)
print(guest_remains.title() + ", я сожалею об отмене приглашения.")

guest_remains = guest_list.pop(0)
guest_it_remains.append(guest_remains)
print(guest_remains.title() + ", я сожалею об отмене приглашения.")

guest_remains = guest_list.pop(1)
guest_it_remains.append(guest_remains)
print(guest_remains.title() + ", я сожалею об отмене приглашения.")

print(guest_it_remains)

for name in guest_list:
    print(name.title() + ", приглашение остаётся в силе")

del guest_list[-1]
print(guest_list)

del guest_list[-1]
print(guest_list)
print("Количество гостей в упражнении 3-7:", len(guest_list))
