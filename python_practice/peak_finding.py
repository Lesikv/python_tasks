#!usr/bin/env python
#coding: utf-8

def peak_finding(arr):
    """
    Let's call an array A a mountain if the following properties hold:
    A.length >= 3
    There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    """
    print arr
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            print i
            return i



def test():
    assert peak_finding([0, 1, 0]) == 1

def test_1():
    assert peak_finding([0,2,1,0]) == 1

if __name__ == '__main__':
    test()
    test_1()
