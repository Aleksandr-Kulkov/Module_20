'''Программа получает от пользователя имя файла, открывает этот файл в текущем каталоге, читает его и выводит два слова:
наиболее часто встречающееся из тех, что имеют размер более трех символов,
и наиболее длинное слово на английском языке.'''

# Принимаем имя файла от пользователя
name = input("Введите имя файла: ")

# Открываем файл. Считываем текст. Убираем переводы строки. Разбиваем текст построчно на список слов.
list_of_strings = []
with open(name, 'rt', encoding="utf8") as myFile:
    for line in myFile:
        list_of_strings.append(line.replace('\n', '').split(' '))

# Объединяем построчные списки слов в список слов. Переводим слова в нижний регистр.
words = []
for i in list_of_strings:
    words.extend(i)
words = list(map(str.lower, words))

# Определяем наиболее часто встречающееся слово из тех, что имеют размер более трех символов
frequent_word = words[0]
for word in words:  # для каждого слова в списке слов проверяем
    if len(word) > 3:  # если размер слова более трех символов
        count = words.count(word)  # тогда считаем количество вхождений слова в список
        if count >= words.count(frequent_word):  # если слово повторяется чаще, либо также часто, как предыдущее
            frequent_word = word  # записываем слово в переменную
print("Наиболее часто встречающееся слово размера более трех символов: ", frequent_word)

alpha_eng = 'abcdefghijklmnopqrstuvwxyz'  # строка с латиницей в нижнем регистре
eng_words = []  # список английских слов


# Функция определяет, состоит ли слово из английских букв
def eng(word):
    for char in word:
        if char in alpha_eng:
            return True
        else:
            return False


#  Для каждого слова в списке слов проверяем
for word in words:
    if eng(word):  # если слово состоит из английских букв
        eng_words.append(word)  # добавляем слово в список английских слов

#  Ищем наиболее длинное слово на английском языке
longest = eng_words[0]
for word in eng_words:  # для каждого слова в списке английских слов проверяем
    if len(word) >= len(longest):  # если слово длиннее, либо равно по длине предыдущему
        longest = word  # записываем слово в переменную
print("Наиболее длинное слово на английском языке: ", longest)