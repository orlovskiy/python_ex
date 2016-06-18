#!/usr/bin/python3
#encoding: utf-8

__author__ = 'Отзовись, автор ;)'

"""Упражнение "Количество слов"

Функция main() ниже уже определена и заполнена. Она вызывает функции 
print_words() и print_top(), которые вам нужно заполнить.

1. Если при вызове файла задан флаг --count, вызывается функция 
print_words(filename), которая подсчитывает, как часто каждое слово встречается 
в тексте и выводит:
слово1 количество1
слово2 количество2
...

Выводимый список отсортируйте в алфавитном порядке. Храните все слова 
в нижнем регистре, т.о. слова "Слон" и "слон" будут обрабатываться как одно 
слово.

2. Если задан флаг --topcount, вызывается функция print_top(filename),
которая аналогична функции print_words(), но выводит только топ-20 наиболее 
часто встречающихся слов, таким образом первым будет самое часто встречающееся 
слово, за ним следующее по частоте и т.д.

Используйте str.split() (без аргументов), чтобы разбить текст на слова.

Отсекайте знаки припинания при помощи str.strip() с знаками припинания 
в качестве аргумента.

Совет: не пишите всю программу сразу. Доведите ее до какого-то промежуточного 
состояния и выведите вашу текущую структуру данных. Когда все будет работать 
как надо, перейдите к следующему этапу.

Дополнительно: определите вспомогательную функцию, чтобы избежать дублирования 
кода внутри print_words() и print_top().

"""

import sys
import codecs


def make_dic(filename):     # 2016.03.23_01:12:58 checked. prusanov
    textfile = open(filename,'r')
    text_from_file = textfile.read()
    text_from_file = unicode(text_from_file, 'utf-8').lower() #переводим в lowercase
    split = ["!",".","?",",",":","-","+"]                     # то, что хотим убрать из текста. Можно ли передать все это не циклу, а скажем программе типа ".replace" ?
    for x in split:
        text_from_file = text_from_file.replace(x," ")        # Вырезаем нежелательные символы
    words = text_from_file.split()                            # Нарезаем по словам
    pre_dic = set(words)                                      # Исключаем повторы
    dic = dict.fromkeys(pre_dic,0)                            # Создаем словарь
    what_to_search = dic.keys()                               # что бы не вызывать каждый раз dic.keys() в цикле ниже

    for x in words:                                           #Перебираем список слов, прибавляя 1 к соответствующему элементу словаря dic
        if x in what_to_search:         # эта проверка получается лишней, т.к. раньше уже порядком всё провернули ;)
            dic[x] +=1



    return dic



def print_words(filename):      # 2016.03.23_01:18:46 checked. prusanov
    dic = make_dic(filename)
    wordlist = sorted(dic.items())

    for x in wordlist:
        print x[0], x[1]



def print_top(filename):        # 2016.03.23_01:19:01 checked. prusanov
    dic = make_dic(filename)
    wordlist = sorted(dic.items(), key = lambda x : x[1], reverse = True)[:20]

    for x in wordlist:
        print x[0], x[1]



# +++ваш код+++
# Определите и заполните функции print_words(filename) и print_top(filename).
# Вы также можете написать вспомогательную функцию, которая читает файл,
# строит по нему словарь слово/количество и возвращает этот словарь.
# Затем print_words() и print_top() смогут просто вызывать эту вспомогательную функцию.

###

# Это базовый код для разбора аргументов коммандной строки.
# Он вызывает print_words() и print_top(), которые необходимо определить.
def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
    main()
