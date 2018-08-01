#usr/bin/env python
#coding:utf-8

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

k = a if a < b else b
print k

while (a % k != 0) or (b % k != 0):
    k -= 1
print k
