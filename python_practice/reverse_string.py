#!usr/bin/env python
#coding: utf-8


s = input('Введите строку ')

def reverse_string(s):
    s = list(s)
    i = 0
    while i < len(s) / 2:
        s[i], s[-i - 1] = s[-i - 1], s[i]
        i += 1
    return ''.join(s)


if __name__ == '__main__':
    print reverse_string(s)
