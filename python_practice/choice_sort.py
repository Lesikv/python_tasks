#!usr/bin/env python
#coding: utf-8


def find_smallest(src):
    min = src[0]
    min_idx = 0

    for i in range(1, len(src)):
        if src[i] < min:
            min = src[i]
            min_idx = i

    return min_idx

def find_max(src):
    max = None
    max_idx = None

    for i in range(len(src)):
        curr = src[i]

        if curr > max:
            max = curr
            max_idx = i

    return max_idx


def selection_sort(src):
    sorted = []

    for i in range(len(src)):
        min_idx = find_smallest(src)
        sorted.append(src.pop(min_idx))

    return sorted






if __name__ == '__main__':
   #print find_max([8,2,5,6,4, 10])

   print selection_sort([5, 7, 1000, 9, 8, 1, 9])
