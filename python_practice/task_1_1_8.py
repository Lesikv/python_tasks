#usr/bin/env python
#coding: utf-8

n = int(input('Введите n '))

def fact(n):
    if n == 0:
        return  1
    return fact(n-1)*n


#print fact(n)

fact = lambda n: 1 if n == 0 else fact(n-1)*n
print fact(n)
