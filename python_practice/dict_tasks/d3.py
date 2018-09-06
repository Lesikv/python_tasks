#!/usr/bin/env python
#coding: utf-8

import datetime

YEAR = datetime.date.today().year

STATS = [
            {'brand': 'Mercedes-Benz', 'foundation_year': 1926, 'stats': {'produced_cars': 20000000}},
            {'brand': 'Volkswagen', 'foundation_year': 1937, 'stats': {'produced_cars': 13000000}},
            {'brand': 'Škoda Auto', 'foundation_year': 1895, 'stats': {'produced_cars': 25000000}},
        ]



def count_cars(src):
    """
    Из данного массива:
    получить по каждому бренду среднее количество продаваемых маниш за один год
    
    """
    res = {}
    for elem in src:
       # print elem
        key = elem['brand']
        #print key
        if key not in res:
            res[key] = {'avg_cars': 0}
        res[key]['avg_cars'] = elem['stats']['produced_cars'] / (2018 - elem['foundation_year'])


    print res



    


if __name__ == '__main__':
    print count_cars(STATS)
