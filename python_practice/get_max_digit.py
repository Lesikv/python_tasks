#!usr/bin/env python
#coding: utf-8


number = int(input('Введите число '))

def get_max_digit(number):
    """
    :type number: int
    :rtype: int
    """
    i = 0
    while number != 0:
        i += 1
        number /= 10
                                                    
    return i

print get_max_digit(number)


def get_digit(number, i):
    return (number / 10**(i)) % 10

if __name__ == '__main__':
    for i in range(get_max_digit(number)):
        print get_digit(number, i)
