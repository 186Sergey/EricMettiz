
"""
Упражнение 4-10
Срезы.
Добавить в конец одной из программ, написанных в этой главе, фрагмент, который делает следующее:
    выводит сообщение "Первыми тремя пунктами в списке являются:", а затем использует срез для вывода первых трёх
    элементов из списка;
    выводит сообщение "Тремя пунктами из середины списка являются:", а затем использует срез для вывода первых трёх
    элементов из середины списка;
    выводит сообщение "Последними тремя пунктами в списке являются:", а затем использует срез для вывода последних трёх
    элементов из середины списка;
"""

players = ['антон', 'николай', 'владимир', 'елена', 'ольга']
print("Первыми тремя пунктами в списке являются:")
print(players[:3])

print("\nТремя пунктами из середины списка являются:")
print(players[1:4])

print("\nПоследними тремя пунктами в списке являются:")
print(players[2:])
