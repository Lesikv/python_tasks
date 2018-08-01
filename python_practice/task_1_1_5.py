#usr/bin/env python
#coding:utf-8

a = int(input('Введите a '))
b = int(input('Введите b '))

res = a 
for i in range(1, b+1):
    res = res + i 

print res
