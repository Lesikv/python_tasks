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

n = Node('a', Node('b', Node('c', Node('d', Node('c')))))

print n
