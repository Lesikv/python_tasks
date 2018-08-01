#!usr/bin/env python
#coding: utf-8

divider = 10
#source = int(input('Введите число '))
#digit = int(input('Введите разряд числа '))


def get_digit(num, l):
    print 'New launch'
    k = 0
    while num :
        print 'YAHOO 1', num, l, k
        if k == l - 1: 
            print 'YAHOO 2', num, l, k
         #   print 'YAHOO'
            return num % divider
        num //= divider
        print 'YAHOO 3', num, l, k
        k += 1
        print 'YAHOO 4', num, l, k
    #if num == 0:
    return 0

def get_digit2(num, l):
    return (num // divider**(l-1)) % divider



if __name__ == '__main__':
    if get_digit(153, 2) != 5:
        print 'Неверный результат на произвольном значении' 
    if get_digit(0, 1) != 0:
        print 'Неверный результат на значении = 0'
    if get_digit(153, 10) != 0:
        print 'Неправильный результат при значении больше фактического разряда'

    if get_digit2(153, 2) != 5:
        print 'Неверный результат на произвольном значении' 
    if get_digit2(153, 10) != 0:
        print 'Неправильный результат при значении больше фактического разряда'

    if get_digit2(0, 1) != 0:
        print 'Неверный результат на значении = 0'
