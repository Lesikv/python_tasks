#!usr/bin/env python
#coding: utf-8

def is_power(num):
    """
    Given a positive integer which fits in a 32 bit signed integer, 
    find if it can be expressed as A^P where P > 1 and A > 0. 
    A and P both should be integers.
    """
    if num == 0:
        return False
    if num == 1:
        return True
    for p in range(2, 33):
        for res in range(2, int(num**(1.0/p)) + 2):
            if res**p == num:
                return True
    return False


def test():
    assert is_power(16) == True
    assert is_power(20) == False


if __name__ == '__main__':
    print is_power(18)

