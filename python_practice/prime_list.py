#!/usr/bin/env python
#coding: utf-8

def is_prime(n):
    """
    Функция, которая генерирует список простых чисел меньших n
    @param num: int
    @return list
    """
    primes = [1 for i in range(n+1)]
    primes[0] = 0
    primes[1] = 0
    for i in range(2, n+1):
        j = 2
        if primes[i] == 1:
            while i*j <n:
                primes[i*j] = 0
                j += 1
    return primes

def prime_sum(n):
    primes = is_prime(n)
    for i in range(2, len(primes)):
        if primes[n - i] == 1 and primes[i] == 1:
            return i, n - i

def test():
    assert is_prime(3) == [0, 0, 1, 1]
def test2():
    assert is_prime(5) == [0, 0, 1, 1, 0, 1]

if __name__ == '__main__':
    test()
    test2()
    print prime_sum(10)



