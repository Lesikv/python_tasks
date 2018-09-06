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
    
    for i in range(len(k)):
        key = k[i]
        if key not in res:
            res[key] = ''
        if i < len(v):
            res[key] = v[i]
        else:
            res[key] = None

    #res = dict(zip(k,v))
    #res.values().extend([None]*(len(k) - len(v)))

    return res


if __name__ == '__main__':
    print create_dict(KEYS, VALUES)


