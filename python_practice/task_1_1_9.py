#usr/bin/env python
#coding: utf-8

n = int(input('Введите n ')) 

res = []
def fib(n):
    if n == 0:
        print 'Yahoo'
        return 0
    elif n == 1:
        return 1
    return fib(n-2) + fib(n-1)

def fib2(n):
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b
    return a

print fib2(n)
