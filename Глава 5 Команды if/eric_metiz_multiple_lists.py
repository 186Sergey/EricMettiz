"""
Множественные списки
Посетители способны заказать что угодно, особенно когда речь заходит о дополнениях к пицце. Что если клиент захочет
положить на пиццу картофель фри? Списки и команды if позволят убедиться в том, что выходные данные имеют смысл,
прежде чем обрабатывать их.
Проверим наличие нестандартных дополнений перед тем, как готовить пиццу. В следующем примере определяются два списка.
Первый список содержит перечень доступных дополнений, а второй - список дополнений, заказанных клиентом. На этот раз
каждый элемент из requested_toppings проверяется по списку доступных дополнений перед добавлением в пиццу
"""

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Добавлено " + requested_topping + ".")
    else:
        print("Извините, у нас нет " + requested_topping + ".")

print("\nЗакончил готовить свою пиццу!")
