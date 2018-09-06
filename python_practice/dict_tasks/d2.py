#!/usr/bin/env python
#coding: utf-8


SOURCE = {'Война и мир': 'Толстой', 'Анна Каренина': 'Толстой', 'Герой нашего времени': 'Лермонтов'}


def books(src):
    """
    Дан словарь соответствий книг авторам. Необходимо из него составить 
    словарь соответствия авторов всем их книгам
    """

    authors = src.values()
    res = {}
    for aut in authors:
        key = aut
        if key not in res:
            res[key] = []

        for book in src.keys():
            if src[book] == key:
                res[key].append(book)
    return res





if __name__ == '__main__':
    print books(SOURCE)
