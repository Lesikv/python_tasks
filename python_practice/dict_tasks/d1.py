#!/usr/bin/env python
#coding: utf-8

KEYS = ['a', 'b', 'c']
VALUES = [0, 1]

def create_dict(k, v):
    """
    Есть два списка разной длины. В первом содержатся ключи, а во втором значения. Напишите функцию, 
    которая создаёт из этих ключей и значений словарь. Если ключу не хватило значения, в словаре должно быть 
    значение None. Значения, которым не хватило ключей, нужно игнорировать.
    """
    res = {}
    
    res = dict(zip(k,v))
    res.values().extend([None]*(len(k) - len(v)))

    return res


if __name__ == '__main__':
    print create_dict(KEYS, VALUES)


