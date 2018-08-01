#!usr/bin/env python
#coding: utf-8

def binary_search(array, num):
    """
    Бинарный поиск в массиве
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = array[mid]

        if guess == num:
            return mid
        if mid < num:
            low = mid + 1
        if mid > num:
            high = mid - 1
    return None

if __name__ == '__main__':
    print binary_search([1,2,5,7,9,11], 6)
