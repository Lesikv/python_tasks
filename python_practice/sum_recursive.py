#usr/bin/env python
#coding: utf-8

def sum_recursive(lst):
    """
    Найти рекурсивную сумму элементов списка
    """
    if lst == []:
        return 0
    print lst[0]
    print lst[1:]
    return lst[0] + sum_recursive(lst[1:])

print sum_recursive([1,3,4,5])






