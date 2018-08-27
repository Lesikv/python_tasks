#!/usr/bin/env python
#coding: utf-8

ARRAY = [1, 12, 22, 141, 5, 6]


def get_max_digit(n):
    """
    Функция, возвращающая максимальный разряд числа
    """
    i = 0
    while n != 0:
        i += 1
        n /= 10
    
    return i


def get_digit(n, i):
    """
    Функция, возвращающая значение i-го разряда
    """
    return (n / 10**i) % 10 


def check_sum(n):
    """
    Проверяет, является ли сумма цифр в числе четным числом
    """
    sum = 0
    for i in range(get_max_digit(n)):
        sum += get_digit(n, i)
    if sum % 2 == 0:
        return True
    return False

def check_arr(arr):
    """
    Для массива чисел вывести те, сумма цифр которого является четным числом.
    """
    res = []
    for elem in arr:
        if check_sum(elem):
            res.append(elem)
    return res




if __name__ == '__main__':
    print get_max_digit(141)
    print get_digit(141, 2)
    print check_sum(141)
    print check_arr(ARRAY)

