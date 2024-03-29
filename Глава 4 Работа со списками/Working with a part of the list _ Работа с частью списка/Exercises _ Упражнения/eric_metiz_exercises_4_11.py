
"""
Упражнение 4-11
Моя пицца, твоя пицца.
Начать с программы из упражнения 4-1. Создать копию списка с видами пиццы, присвоив ему имя friend_pizzas. Затем
сделать следующее:
    добавить новую пиццу в исходный список;
    добавить другую пиццу в список friend_pizzas;
    доказать, что в программе существует два разных списка. Вывести сообщение "Мои любимые виды пиццы - это:", а
    затем первый список в цикле for.
    вывести сообщение "Любимая пицца моего друга - это:", а затем второй список в цикле for. Убедиться в том, что
    каждая новая пицца находится в соответствующем списке.
"""

pizzas = ['пеперони', 'маргарита', 'маринара', 'четыре сыра', 'каприччиоза']
friend_pizzas = pizzas[:]
print("Оригинальный список пиццы: ", pizzas)

pizzas.append('наполлетана')
friend_pizzas.append('фритта')

print("\nМои любимые виды пиццы - это:")
for i in pizzas:
    print(i.title())

print("\nЛюбимая пицца моего друга - это:")

for j in friend_pizzas:
    print(j.title())
