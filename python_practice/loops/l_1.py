#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_sum(N):
    """
    Вывести сумму чисел от 1 до N. Без использования sum)
    """
    sum_res = 0
    if N <= 0:
        return 0
    for i in xrange(1, N + 1):
        sum_res += i
    return sum_res


def test_zero():
    assert print_sum(-1) == 0
    
def test_negative():
    assert print_sum(-1) == 0

def test():
    assert print_sum(5) == 15

if __name__ == '__main__':
    test_zero()
    test_negative()
    test()
    print print_sum(10)


