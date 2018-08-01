#usr/bin/env python
#coding: utf-8

import argparse
import sys

parser = argparse.ArgumentParser(description = 'Input array, index_from and index_to')
parser.add_argument('integers', type=int, nargs='+')
#parser.add_argument('--array', action = 'append')
parser.add_argument('--id_from', type=int)
parser.add_argument('--to', type=int)

for line in sys.stdin:
     source = map(int, line.split(' '))
     break

print source


#TODO: использовать stdin или свободные агрументы  nargs = '+'
#array = [1,2,3,4,5,6,7,8,9,10]
# for line in sys.stdin
def build_sum_arr(arr):
    #elem = arr[0]
    arr_sum = [0]
    for i in range(len(arr)):
        arr_sum.append(arr_sum[i] + arr[i])
    print 'SOURCE: {}, SUM: {}'.format(arr, arr_sum)
    return arr_sum

def get_sum(arr,index_from, index_to):
    res = arr[index_to] - arr[index_from - 1]
    
    print 'Result: {}'.format(res)
    return res

if __name__ == '__main__':
    options = parser.parse_args()
    array = options.integers
    #array = [ int(i) for i in options.array]
    #построение индекса нужно разделять с получением данных
    #на одно построение индекса можно вызывать несколько get
    arr_sum = build_sum_arr(array)
    index_from = options.id_from
    index_to = options.to
    print 'FROM: {}, TO: {}'.format(index_from, index_to)
    get_sum(arr_sum, index_from, index_to)

