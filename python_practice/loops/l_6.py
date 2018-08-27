#!/usr/bin/env python
#coding: utf-8

ARRAY = [10, 6, 5, 0, 10, 1]

def find_max(arr):
    """
    Для массива чисел найти первое такое, 
    которое больше суммы всех предыдущих (если нет таких, что None)
    """
    sum = 0
    res = None

    for i in range(1, len(arr)):
        sum += arr[i-1]
        if arr[i] > sum:
            return arr[i]


if __name__ == '__main__':
    print find_max(ARRAY)
