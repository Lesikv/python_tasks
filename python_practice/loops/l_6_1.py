#!/usr/bin/env python
#coding: utf-8

ARRAY = [10, 6, 17, 5, 30, 20, 1, 100, 0]

def find_max(arr, n):
    """
    Для массива чисел найти первых два числа таких что, 
    которое больше суммы всех предыдущих (если нет таких, что None)
    """
    sum = 0
    res = []
    for k in range(n):
        for i in range(1, len(arr)):
            sum += arr[i-1]
            if arr[i] > sum:
                res.append(arr[i])
    return res


if __name__ == '__main__':
    print find_max(ARRAY, 3)
