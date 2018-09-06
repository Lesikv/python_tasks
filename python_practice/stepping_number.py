#!/usr/bin/env/python
#coding: utf-8

N, M = 10, 20

def stepping_number(N, M):
    """
    Given N and M find all stepping numbers in range N to M
    A number is called as a stepping number if the adjacent digits have a difference of 1.
    e.g 123 is stepping number, but 358 is not a stepping number
    """
    
    res = [] 
    for num in range(N, (M + 1)):
#        print num
        prev = (num // 1) % 10
 #       print prev
        i = 1
        while num // 10**i > 0:
  #          print res
            curr = (num // 10**i ) % 10
   #         print curr
            if abs(curr - prev) != 1:
                print 'NE OK'
                break
            res.append(num)
            prev = curr
            i += 1
    return res


if __name__ == '__main__':
    print stepping_number(N, M)
    
