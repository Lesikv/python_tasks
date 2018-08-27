#!/usr/bin/env python
#coding: utf-8

n = input('Введите число ')

while True:
    if isinstance(n, int):
        print n ** 2
        break
    elif n == 'exit':
        break
    else:
        print 'Вы ввели не число'
        break


