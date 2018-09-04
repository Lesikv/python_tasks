#!/usr/bin/env python
#coding:utf-8


MATRIX = [[1,2,3], [4,5,6], [7,8,9]]

def antidiag(arr):
    m = len(arr)
    # количество строк
    n = len(arr[0])
    # количество столбцов
    res = [[] for i in range(m + n - 1)]
    #print res
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print i + j - 2
            print i, j, arr[i - 1][j - 1]
            res[i + j - 2].append(arr[i - 1][j - 1])
    return res



if __name__ == '__main__':
    print antidiag(MATRIX)



