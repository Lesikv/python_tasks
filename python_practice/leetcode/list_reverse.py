#!usr/bin/env python
#coding: utf-8

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.next:
            return self.val
        return '{} -> {}'.format(self.val, self.next)
    
    def __eq__(self, other):
        return self.val == other.val and self.next.val == other.next.val


n = Node('a', Node('b', Node('c', Node('d'))))

print n

def list_reverse(lst):
    prev_n = None
    next_n = lst.next
    while True:
        lst.next = prev_n
        if not next_n:
            break
        prev_n = lst
        lst = next_n
        next_n = lst.next
        print 'prev_n  = {}, lst = {}, next_n = {}'.format(prev_n, lst, next_n)
    return lst


def test():
    lst_for_check =  Node('d', Node('c', Node('b', Node('a'))))
    #print lst_for_check
    assert list_reverse(n) == lst_for_check
    # операция сравнения

if __name__ == '__main__':
    test()
    #print list_reverse(n)


