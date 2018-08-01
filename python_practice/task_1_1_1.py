#usr/bin/env python
#coding: utf-8


a = int(input('Введите a '))
b = int(input('Введите b '))

print 'a before {}, b before {}'.format(a,b)

temp = a
a=b
b=temp


print 'a after {}, b after {}'.format(a,b)


