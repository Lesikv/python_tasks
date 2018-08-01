#!usr/bin/env python
#coding: utf-8

n = int(input('Введите n '))
def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)

print fact(n)
