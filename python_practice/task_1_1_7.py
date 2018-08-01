#!/usr/bin/env python
#coding: utf-8

a = int(input('Введите a '))
d = int(input('Введите d '))


r = a 
q = 0


while r >= d:
    r -= d
    q += 1

print 'r = {}, q = {} '.format(r, q)


