#!usr/bin/env python
#coding: utf-8




def merge(arr, tmp, l, m, r):
    aptr = l
    bptr = m
    i = l
    while (aptr < m and bptr <= r ):
        if arr[aptr] < arr[bptr]:
            tmp[i] = arr[aptr]
            i += 1
            aptr += 1
        else:
            tmp[i] = arr[bptr]
            i += 1
            bptr += 1
    while (aptr < m ):
        tmp[i] = arr[aptr]
        i += 1
        aptr += 1
    while (bptr <= r):
        tmp[i] = arr[bptr]
        i += 1
        bptr += 1
    
    for k in range(l, r + 1):
        arr[k] = tmp[k]
    

def merge_sort(arr, tmp, l, r):
    if l < r:
        mid = (l + r) / 2
        merge_sort(arr, tmp, l, mid)
        merge_sort(arr, tmp, mid + 1, r)
        merge(arr, tmp, l, mid + 1, r)
    return arr

def test_merge_sort():
    arr = [2,1]
    tmp = [0]*2
    merge_sort(arr, tmp, 0, 1) 
    print arr
    assert arr == [1,2]

def test_merge_sort_2():
    arr = [2, 5, 1, 4, 0]
    tmp = [0]*5
    merge_sort(arr, tmp, 0, 4)
    print arr
    assert arr == [0, 1, 2, 4, 5]

def test_merge_2():
    arr = [0, 1, 4, 2, 5]
    tmp = [0]*5
    merge(arr, tmp, 0, 3, 4)
    print arr

    assert arr == [0, 1, 2, 4, 5]

def test_merge():
    arr  = [2,1]
    tmp = [0] * 2
    merge(arr, tmp, 0, 1, 1)
    print arr
    assert arr == [1, 2] 

if __name__ == '__main__':
    test_merge()
    test_merge_sort()
    print 'OK, small test'
    test_merge_2()
    test_merge_sort_2()
    print 'OK, big test'



