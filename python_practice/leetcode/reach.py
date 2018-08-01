#!/usr/bin/env python
#coding: utf-8

def reach(x, y):
    """
    You are in an infinite 2D grid where you can move in any of the 8 directions 
    You are given a sequence of points and the order in which you need to cover the points. 
    Give the minimum number of steps in which you can achieve it. You start from the first point.
    Input : [(0, 0), (1, 1), (1, 2)]
    Output : 2
    """
    steps = 0
    n = len(x)
    if len(x) != len(y):
        return None
    for i in range(1,n):
        steps =  max(abs(x[i] - x[i -1]), abs(y[i] - y[i-1]))
    return steps



def test():
    assert reach([0, 1, 1], [0, 1, 2]) == 2


if __name__ == '__main__':
    test()



    
