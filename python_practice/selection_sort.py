#usr/bin/env python
#coding: utf-8


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
            j += 1
        tmp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = tmp
    return arr


print selection_sort([2, 5, 1, 3, 2,  9, 6])

