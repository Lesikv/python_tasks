#!usr/bin/env python
#coding: utf-8


def matrix_transpose(src):
    """
    Given a matrix A, return the transpose of A
    The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
    """
    r, c = len(src), len(src[0])
    res = [[None] * r for i in range(c)] 
    for i in range(len(src)):
        for j in range(len(src[i])):
            res[j][i] = src[i][j]
    return res




def test_1():
    assert matrix_transpose([[1], [2]]) == [[1, 2]]
def test_2():
    assert matrix_transpose([[1, 2], [3, 4]]) == [[1, 3], [2,4]] 

if __name__ == '__main__':
    test_1()

    test_2()
