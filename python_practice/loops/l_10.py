#!/usr/bin/env python
#coding: utf-8

try:
    N = int(input('Введите число '))
except NameError:
    print 'Вы ввели не число'
    N = 0

def return_square(n):
    return n**2

print return_square(N)

