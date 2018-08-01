#!/usr/bin/env python
#coding: utf-8


def diag_matrix(arr):
    if not arr or len(arr) < 1:
        return None
    l_res = len(arr[0]) + len(arr) - 1
    res = [[] for i in range(l_res)]
    
    i, j = 0, 0 
    
    for i in range(len(arr)):

        while j < len(arr):
    
    
    print 'i = {}, j = {}, res[i+j] = {}, res = {},  arr[i][j] = {}'.format(i, j, res[i+j], res, arr[i][j])

    return res


if __name__ == '__main__':
    print diag_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
