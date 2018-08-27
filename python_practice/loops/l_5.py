#!/usr/bin/env python
#coding: utf-8

def print_pyramyd(N):
    k = 0
    while k < N:
        k += 1
        for i in range(k):
            print k,
        print '\n'


if __name__ == '__main__':
    print_pyramyd(5)  
