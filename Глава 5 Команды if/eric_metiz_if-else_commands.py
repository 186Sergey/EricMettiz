
"""
Команды if-else
Часто в программе необходимо выполнить одно действие в том случае, если условие истинно, и другое действие, если оно
ложно. С синтаксисом if-else это возможно. Блок if-else в целом похож на команду if, но секция else определяет
дейстие или набор действий, выполняемых при неудачной проверке.
В следующем примере выводится сообщение, которое выводилось ранее, если возраст достаточен для голосования, но на этот
раз при другом возрасте выводися другое сообщение.
"""

age = 17

if age >= 18:
    print("\nВы достаточно взрослые, чтобы голосовать!")
    print("Вы уже зарегистрировались для голосования?")
else:
    print("Извините, вы слишком молоды, чтобы голосовать")
    print("Пожалуйста, зарегистрируйтесь для голосования, как только вам исполнится 18 лет!")

"""
Этот код работает, потому что существует всего две возможные ситуации: возраст либо достаточен для голосования, либо 
недостаточен. Структура if-else хорошо подходит для тех ситуаций, в которых Python всегда выполняет только одно из двух 
возможных действий. В подобных простых цепочках if-else  всегда выполняется одно из двух возможных действий.
"""