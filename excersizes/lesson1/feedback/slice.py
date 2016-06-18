#!/usr/bin/python3
#encoding: utf-8            # 2016.03.19_08:54:09 checked. prusanov  -- # coding: utf-8
# Срезы

# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.

# Справвка
# Оператор получения среза имеет три формы записи: 
# seq[start]
# seq[start:end]
# seq[start:end:step]
# Шаг может быть отрицательным, в этом случае элементы последовательности
# вернутся в обратном порядке.


# A. Четные
# Дана строка, состоящая из символов и/или последовательностей символов, 
# разделенных пробелами.
# Нужно вернуть строку, содержащую только четные элементы из исходной строки.
# Например, из 'a b c d e f' получится 'b d f'
# Решите задачу в одну строчку используя срезы.
def even(s):        # 2016.03.19_08:54:42 checked. prusanov
    return " ".join(s.split(" ")[1::2])


# B. Наоборот
# Дана строка, состоящая из символов и/или последовательностей символов,
# разделенных пробелами.
# Нужно вернуть строку, содержащую элементы исходной строки в обратном порядке.
# Например, из 'a b c d e' получится 'e d c b a'
# Решите задачу в одну строчку используя срезы.
def reverse(s):     # 2016.03.19_08:54:47 checked. prusanov
    return " ".join(s.split(" ")[::-1])


# C. Сдвиг
# Дана строка, состоящая из символов и/или последовательностей символов, 
# разделенных пробелами.
# Нужно вернуть строку, в которой последний элемент находится на первом месте.
# Например, из 'a b c d e f' получится 'f a b c d e'
# Решите задачу в две строки используя срезы.
def shift(s):           # 2016.03.19_08:54:59 checked. prusanov
                        # имеет смысл вынести s.split(" ") в отдельную переменную
    return s.split(" ")[-1] + " " + " ".join(s.split(" ")[0:-1])


# D. Палиндром
# Дано число.
# Нужно определить является ли оно палиндромом.
# Число является палиндромом если оно одинаково читающееся в обоих направлениях.
# Решите задачу в одну строку используя срезы.
def palindrome(d):    # 2016.03.19_08:55:38 checked. prusanov
                # немного усложнили с join'ом
                # return str(d)[::-1] == str(d)
    return "".join(str(d)[::-1][0:len(str(d))/2]) == "".join(str(d)[:len(str(d))/2:1]) # можно проверить и текстлвые палиндромы, но только на литинице. Не разобрался с кодировкой пока


# E. Внутри
# Дана строка, состоящая из четного количества символов и/или последовательностей символов,
# разделенных пробелами.
# Верните строку, в которой первый и последний элементы поставлены в середину 
# исходной строки. Например, из 'a b c d e f' получится 'b c a f d e'.
# Решите задачу в три строки используя срезы.
def inside(s):      # 2016.03.19_08:58:15 checked. prusanov
    literals = s.split(" ")
    middle=len(s.split(" "))/2
    result = " ".join(literals[1:middle]) + " " + literals[0] + " " + literals[-1] + " " + " ".join(literals[middle:-1])
    return result



# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает фунции выше с тестовыми параметрами.
def main():
    print('Четные')
    test(even('a b c d e f'), 'b d f')
    test(even('w ee rt fff xyz'), 'ee fff')

    print()
    print('Наоборот')
    test(reverse('a b c d e f'), 'f e d c b a')
    test(reverse('w ee rt fff xyz'), 'xyz fff rt ee w')

    print()
    print('Сдвиг')
    test(shift('a b c d e f'), 'f a b c d e')
    test(shift('w ee rt fff xyz'), 'xyz w ee rt fff')

    print()
    print('Палиндром')
    test(palindrome(12321), True)
    test(palindrome(1001), True)
    test(palindrome(12345), False)

    print()
    print('Внутри')
    test(inside('a b c d e f'), 'b c a f d e')
    test(inside('w ee rt fff'), 'ee w fff rt')


if __name__ == '__main__':
    main()
