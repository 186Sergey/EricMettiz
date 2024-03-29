"""
УПОРЯДОЧЕННЫЙ ПЕРЕБОР КЛЮЧЕЙ СЛОВАРЯ.
Словарь всегда поддерживает связь между ключом и связанным с ним значением, но порядок получения элементов из словаря
непредсказуем. Впрочем, это не создаёт проблем, потому что обычно требуется лишь получить правильное значение,
связанное с каждым ключом.
Один из способов получения элементов в определённом порядке основан на сортировке ключей, возвращаемых циклом for. Для
получения упорядоченной копии ключей можно воспользоваться функцией SORTED():
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", спасибо вам за участие в опросе!")

"""
Эта команда FOR не отличается от других команд for, если не считать того, что метод DICTIONARY.KEYS() ЗАКЛЮЧЁН В 
ВЫЗОВ ФУНКЦИИ SORTED(). Эта конструкция приказывает Python выдать список всех ключей в словаре и отсортировать его 
перед тем, как перебирать элементы. В выводе перечислены все пользователи, участвовавшие в опросе, а их имена 
упорядочены по алфавиту.
"""

