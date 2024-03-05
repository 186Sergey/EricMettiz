
"""
Проверка неравенства.

Если нужно проверить, что два значения различны, используем комбинацию из восклицательного знака и знака равенства (!=).
Восклицательный знак представляет отрицание, как и во многих языках программирования.
Для знакомства с оператором неравенства воспользуемся командой if. В переменной хранится заказанное дополнение к пицце.
Если клиент не заказал анчоусы (anchovies), программа выводит сообщение:
"""

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Поддержи анчоусы!")

"""
В большинстве условных выражений, которые вы будете использовать в программах, будет проверяться равенство, но иногда 
проверка неравенства оказывается более эффективной.
"""