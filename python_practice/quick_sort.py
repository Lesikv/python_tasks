#usr/bin/env python
#coding: utf-8

def quick_sort(arr, l, r):
    if l < r:
        pivot = (l + r) / 2
        i = l
        j = r - 1
        
        arr[pivot], arr[r] = arr[r], arr[pivot]
        pivot = r
        while i < j:
            while (i < r - 1  and arr[i] < arr[pivot]):
                print 'yahoo', pivot, l, r
                i += 1
            print 'YAHOO i = {}, j = {}, arr = {}, pivot = {}'.format(i, j, arr, pivot)
            while (j > 0 and arr[j] > pivot):
                    j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        if i == j and arr[i] < arr[pivot]:
            i += 1 
        arr[i], arr[pivot] = arr[pivot], arr[i]

        print 'YAHOO1 i = {}, j = {}, arr = {}, pivot = {}'.format(i, j, arr, pivot)
        quick_sort(arr, l, i - 1)
        
        print 'YAHOO2 i = {}, j = {}, arr = {}, pivot = {}'.format(i, j, arr, pivot)
        quick_sort(arr, i + 1, r)


def quick_sort_test():
    arr = [2, 1]
    quick_sort(arr, 0, 1)
    print arr
    assert arr == [1, 2]

def quick_sort_test2():
    arr = [2, 1, 5]
    quick_sort(arr, 0, 2)
    print arr
    assert arr == [1, 2, 5]


if __name__ == '__main__':
    quick_sort_test()
    print 'OK first test'
    quick_sort_test2()
    print 'OK second test'
