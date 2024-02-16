
"""
Конкатенация.
Также часто возникает необходимость в объединении строк.
Иногда имя и фамилия находятся в разных переменных и их нужно объединить для вывода полного имени:
"""

first_name = "eric"
last_name = "metiz"
full_name = first_name + " " + last_name
print(full_name.title())

# Болеее сложный пример кокатенации

print("Hello, " + full_name.title() + "!")
# Вывод: Hello, Eric Metiz!
