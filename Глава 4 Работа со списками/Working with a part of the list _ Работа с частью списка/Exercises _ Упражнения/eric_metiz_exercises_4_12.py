
"""
Упражнение 4-12
Больше циклов.
Во всех версиях foods.py из этого раздела мы избегали использования цикла for при выводе для экономии места. Выбрать
версию foods.py и написать два цикла for для вывода каждого списка.
"""

pizzas = ['пеперони', 'маргарита', 'маринара', 'четыре сыра', 'каприччиоза']
friend_pizzas = pizzas[:]

for my_pizza in pizzas:
    print(my_pizza.title())

for friend_pizza in friend_pizzas:
    print(friend_pizza.title())

