#usr/bin/env python
#coding:utf-8

a = int(input('Введите a '))
b = int(input('Введите b '))

print 'a before {}, b before {}'.format(a,b)

a = a + b

print a

b = a - b

print b

a = a - b

print 'a after {}, b after {}'.format(a,b)
