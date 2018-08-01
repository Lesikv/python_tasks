#usr/bin/env python
#coding: utf-8

n = int(input('Введите n '))

def fact(n):
    if n == 0:
        return 1
    return fact(n-1)*n


print fact(n)
res_sum = 1
for i in range(1, n+1):
    res_sum += 1.0/fact(i)

print res_sum 
