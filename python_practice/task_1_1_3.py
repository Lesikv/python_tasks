#usr/bin/env python
#coding: utf-8

from functools import reduce
a = int(input('Введите a '))
n = int(input('Введите n '))

#k = 0
#while k <= n:
 #   if k == 0:
  #      res = 1
   #     k += 1
    #else:
     #   res = res*a
      #  k += 1

res = 1
for i in range(1,n+1):
    res *= a


print res
