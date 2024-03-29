"""
ПЕРЕБОР СЛОВАРЯ.

Словарь Python может содержать как несколько пар "КЛЮЧ-ЗНАЧЕНИЕ", так и миллионы таких пар. Поскольку в словаре может
храниться большой объём данных, Python предоставляет средства для перебора элементов словаря. Информация может храниться
в словарях по-разному, поэтому предусмотрены разные способы перебора. Программа может перебрать все пары
"КЛЮЧ-ЗНАЧЕНИЕ" в словаре, только ключи или только значения.

ПЕРЕБОР ВСЕХ ПАР "КЛЮЧ-ЗНАЧЕНИЕ"

Прежде чем ознакомиться с разными способами перебора, рассмотрим новый словарь, предназначенный для хранения
информации о пользователе веб-сайта. В следующем словаре хранится имя пользователя, его имя и фамилия:
"""

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

"""
То, что Вы узнали в этой главе, позволит вам обратиться к любому отдельному атрибуту user_0. Но что если вы хотите 
посмотреть ВСЕ данные из словаря этого пользователя? Для этого можно воспользоваться перебором в цикле for:
"""

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

"""
Как видим, чтобы написать цикл for для словаря, необходимо создать имена для двух переменных, в которых будет 
храниться ключ и значение из каждой пары "КЛЮЧ-ЗНАЧЕНИЕ". Этим двум переменным можно присвоить любые имена - с 
короткими однобуквенными именами код будет работать точно так же:
    for k, v in user_0.items():
Вторая половина команды for включает в себя имя словаря, за которым следует вызов метода items(), возвращающий список 
пар "КЛЮЧ-ЗНАЧЕНИЕ". Цикл for сохраняет компоненты пары в указанных переменных. В предыдущем примере мы используем 
переменные для вывода каждого ключа К, за которым следует связанное значение V. "\n" в первой команде print 
гарантирует, что перед каждой парой "КЛЮЧ-ЗНАЧЕНИЕ" в выводе будет вставлена пустая строка.
Снова обратите внимание на то, что пары "КЛЮЧ-ЗНАЧЕНИЕ" НЕ ВОЗВРАЩАЮТСЯ в порядке их хранения в словаре. Python не 
интересует порядок хранения пар "КЛЮЧ-ЗНАЧЕНИЕ" - отслеживаются только связи между отдельными ключами и их значениями.
Перебор всех пар "КЛЮЧ-ЗНАЧЕНИЕ" особенно хорошо работает для таких словарей, как в примере favorite_languages, то есть 
для словарей, хранящих один вид информации со многими разными ключами. Перебрав словарь favorite_languages, получим имя 
каждого человека и его любимый язык программирования. Так как ключ всегда содержит имя, а значение - язык 
программирования, в цикле вместо имён KEY и VALUE используются переменные NAME и LANGUAGE. С таким выбором имён 
читателю кода будет проще следить за тем, что происходит в цикле:
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + ", его любимый язык - это " + language.title() + ".")

"""
Код приказывает Python перебрать все пары "КЛЮЧ-ЗНАЧЕНИЕ" в словаре. В процессе перебора пар ключ сохраняется в 
переменной NAME, а значение - переменной LANGUAGE. С этими содержательными именами намного проще понять, что делает 
команда PRINT().
Всего в нескольких строках кода выводится вся информация из запроса.
Такой способ перебора точно так же работает и в том случае, если в словаре будут храниться результаты опроса тысяч и 
даже миллионов людей.
"""