#!/usr/bin/env python
# -*- coding: utf-8 -*-

ARRAY = [1, -1, 0, 0, 5, 2, 6]


def count_numbers(arr):
    """
    Дан массив чиcел. 
    Вывести количество отрицательных чисел, нулей и положительных чисел в виде кортежа. 
    Постарайся сделать это за один проход.
    """
    res = ()
    pos = 0
    # количество положительных чисел
    neg = 0
    # количество отрицательных чисел
    zer = 0
    # количество нулей
    
    for elem in arr:
        if elem == 0:
            zer += 1
        elif elem < 0:
            neg += 1
        else:
            pos += 1
    return (neg, zer, pos)


def test():
    assert count_numbers([-1, 0, 1]) == (1, 1, 1)   

if __name__ == '__main__':
    test() 
    print count_numbers(ARRAY)
    

