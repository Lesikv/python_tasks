#!/usr/bin/env python
#coding: utf-8


CONV = {'INCH': 2.5400438, 'SPAN': 17.78, 'PALLIST': 7}

INCH = 2.5400438
SPAN = 17.78
#пядь
PALLIST = 7
#паллайст

def converter(src):
    """
    Для значений в сантиметрах от 1 до 10 вывести соответствующие значения в дюймах (2,5400438 cм),
    пядях (~17,78 см), суннах (~3,030303 см), палайстах (~7 см).
    """
    for i in range(1,src + 1):
        yield i, INCH*i, SPAN*i, PALLIST*i

def converter2(src):
    for i in range(1, src + 1):
        yield i, i*CONV['INCH'], i*CONV['SPAN'], i*CONV['PALLIST']




if __name__ == '__main__':
    for i in range(1, 10):
        print list(converter2(i))
