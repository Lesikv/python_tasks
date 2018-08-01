#usr/bin/env python
#coding: utf-8


def count_orders(rows):
    res = {}
    for row in rows:
        key = (row['city'], row['user_id'])
        if key not in res:
            res[key] = (0, 0)
            res[key] += 1
    return res


if __name__ == '__main__':
    rows = [
        {
            'city': '123', 'user_id': '123', 'order_id': '234'
            }
        ]

    print count_orders(rows)
