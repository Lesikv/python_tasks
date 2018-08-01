#usr/bin/env python
#coding: utf-8

import datetime
from datetime import datetime, date, timedelta

#test_input_format =  [(), (), ()]
#test = [('2018-01-01','2018-01-02'), ('2018-01-03', '2018-01-04')]

test = [('2018-01-01','2018-01-03'), ('2018-01-02', '2018-01-04')]

def parse_date(source):
    fmt = '%Y-%m-%d'
    res = datetime.strptime(source,fmt)

    return res

def get_sum_of_intervals(input_list):
    """
    Функция для вычисления интервалов по времени
    Левая граница включена, правая - нет
    """
    input_list.sort(key=lambda x: x[0])
    print 'Input:', input_list
    to_max = input_list[0][1]
    from_time_cur = input_list[0][0]
    print to_max
    sum = 0
    for dates in input_list[1:]:
        from_time = dates[0]
        to_time = dates[1]
        print 'from_time: {}, to_time: {}'.format(from_time, to_time)
        if from_time < to_max:
            to_max = max(to_max, to_time)
        else:
            sum += (parse_date(to_max) - parse_date(from_time_cur)).days
            print sum
            print 'from_time_cur: {}, to_max: {}'.format(from_time_cur, to_max)
            to_max = to_time
            from_time_cur  = from_time
    
    sum += (parse_date(to_max) - parse_date(from_time_cur)).days
    
    return sum
    
if __name__ == '__main__':
    print get_sum_of_intervals(test)


