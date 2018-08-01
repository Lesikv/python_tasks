#!usr/bin/env python
#coding: utf-8


def insertion_sort(arr):
    curr = None
    
    for i in range(len(arr)):
        j = i
        curr = arr[i]
        while j > 0 and arr[j-1] > curr:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = curr
    return arr

print insertion_sort([2,1,4,8, 2])        

