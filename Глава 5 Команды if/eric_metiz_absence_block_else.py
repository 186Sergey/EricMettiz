
"""
Отсутствие блока else.
Python не требует, чтобы цепочка if-elif непременно завершалась блоком else. Иногда блок else удобен, в других
случаях бывает нагляднее использовать дополнительную секцию elif для обработки конкретного условия.
"""

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Стоимость вашего входного билета составляет $" + str(price) + ".")

"""
Блок else "универсален": он обрабатывает все условия, не подходящие не под одну конкретную проверку if или elif, 
причём в эту категорию иногда могут попасть недействительные или даже вредоносные данные. Если имеется завершающее 
конкретное условие, лучше использовать завершающий блок elif и опустить блок else. В этом случае можно быть уверенным 
в том, что код будет выполняться только в правильных условиях.
"""