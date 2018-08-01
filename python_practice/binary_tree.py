#!usr/bin/env python
#coding: utf-8

from collections import deque


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
# Creating Fisrt Tree
root1 = Node(1)
root1.left = Node(3)
root1.right = Node(2)
root1.left.left = Node(5)

root1_1 = Node(1)
root1_1.left = Node(3)
root1_1.right = Node(2)
root1_1.left.left = Node(5)
root1_1.right.left = Node(5)
# Creating second Tree
root2= Node(2)
root2.left = Node(1)
root2.right = Node(3)
root2.left.right = Node(4)
root2.right.right = Node(7)


# Creating result tree for tests
root3 = Node(3)
root3.left = Node(4)
root3.right = Node(5)
root3.left.left = Node(5)
root3.left.right = Node(4)
root3.right.right = Node(7)

def createTree(lst):
    if not lst:
        return 
    root = Node(lst[0])
    queue = deque([root])
    i = 1 
    while i < len(lst):
        cur = queue.popleft()
        if lst[i]:
            print lst[i], 'LEFT', cur.value
            cur.left = Node(lst[i])
            queue.append(cur.left)
        i += 1
        if i >= len(lst):
            break
        if lst[i]:
            print lst[i], 'RIGHT', cur.value
            cur.right = Node(lst[i])
            queue.append(cur.right)
        i += 1
    return root


def compareTree(tree1, tree2):
    res = {'0':{'first': [], 'second':[]}, '1':{'first':[], 'second':[]}}
    stack1 = [tree1]
    stack2 = [tree2]
    cur1 = None
    cur2 = None
    while stack1 and stack2:
        cur1 = stack1.pop()
        cur2 = stack2.pop()
        if cur1.value != cur2.value:
            res['0']['first'].append(cur1.value)
            res['0']['second'].append(cur2.value)
            print res, 'YAHOO1'
            return False
        else:
            res['1']['first'].append(cur1.value)
            res['1']['second'].append(cur2.value)
        if cur1.right:
            stack1.append(cur1.right)
        if cur1.left:
            stack1.append(cur1.left)
        if cur2.right:
            stack2.append(cur2.right)
        if cur2.left:
            stack2.append(cur2.left)
    print res, stack1, stack2
    return not stack1 and not stack2

#def merge(tree1, tree2):
#    stack1 = [tree1]
#    stack2 = [tree2]
#    res = []
#    cur1 = None
#    cur2 = None
#    i = 0
#    while stack1 and stack2:
#        print i
#        cur1 = stack1.pop()
#        cur2 = stack2.pop()
#        if cur1 and cur2:
#            new_v = cur1.value + cur2.value
#            res.insert(i, new_v)
#            i += 1
#            stack1.append(cur1.right)
#            stack1.append(cur1.left)
#            stack2.append(cur2.right)
#            stack2.append(cur2.left)
#        if not cur1:
#            if cur2:
#                res.insert(i, cur2.value)
#                stack2.append(cur2.right)
#                stack2.append(cur2.left)
#                stack1.append(None)
#                stack1.append(None)
#                i += 1
#        elif not cur2:
#            res.insert(i, cur1.value)
#            stack1.append(cur1.right)
#            stack1.append(cur1.left)
#            stack2.append(None)
#            stack2.append(None)
#            i += 1
#
#    return res
#
def check_none(src1, src2):
    sum_res = 0
    if src1:
        sum_res += src1.value
    if src2:
        sum_res += src2.value
    return sum_res

def merge(tree1, tree2):
    root = Node(check_none(tree1, tree2))
    stack1 = [tree1]
    stack2 = [tree2]
    stack3 = [root]

    while stack1 and stack2:
         cur1 = stack1.pop()
         cur2 = stack2.pop()
         cur3 = stack3.pop()
         cur1_left = cur1 and cur1.left
         cur2_left = cur2 and cur2.left
         cur1_right = cur1 and cur1.right
         cur2_right = cur2 and cur2.right
         
         if cur1_left or cur2_left:
            cur3.left = Node(check_none(cur1_left, cur2_left))
            stack1.append(cur1_left)
            stack2.append(cur2_left)
            stack3.append(cur3.left)


         if cur1_right or cur2_right:
            cur3.right = Node(check_none(cur1_right, cur2_right))
            stack3.append(cur3.right)
            stack1.append(cur1_right)
            stack2.append(cur2_right)
    return root








def check():
    print merge(root1, root2)
    assert compareTree(merge(root1, root2), root3)
    #assert compareTree(root1, root1), 'Проверка равенства равных деревьев'
    #assert compareTree(root1, root2) == False, 'Проверка неравенства разных деревьев'
    #assert compareTree(root1, root1_1) == False
    #assert compareTree(root1, createTree([1,3,2,5]))

    print 'Everything is OK'
if __name__ == '__main__':
    check()
