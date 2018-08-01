#!usr/bin/env python
#coding: utf-8

from datetime import datetime, timedelta
import calendar


LIST_FOR_TEST  = [
        '2018-04-01', '2018-05-07', '2018-04-03', '2018-04-02', '2018-04-05', '2018-04-04', '2018-04-07', '2018-05-01',
        '2018-04-09', '2018-04-08', '2018-05-08', '2018-05-09', '2018-04-12', '2018-04-13', '2018-04-30', '2018-04-17', 
        '2018-05-15', '2018-05-14', '2018-05-17', '2018-05-16', '2018-05-11', '2018-05-10', '2018-05-13', '2018-05-29',
        '2018-01', '2018-03', '2018-02', '2018-05-19', '2018-05-18', '2018-04-06', '2018-04-19', '2018-05-28', '2018-04-23',
        '2018-04-29', '2018-04-28', '2018-06-02', '2018-06-01', '2018-04-22', '2018-05-20', '2018-05-21', '2018-04-21',
        '2018-04-20', '2018-04-27', '2018-05-25', '2018-04-25', '2018-04-24', '2018-05-23', '2017-12', '2017-11', 
        '2017-10', '2018-04-26', '2018-05-12', '2018-05-26', '2018-05-27', '2018-05-22', '2018-05-06', '2018-04-18', 
        '2018-05-04', '2018-05-05', '2018-05-02', '2018-05-31', '2018-05-30', '2017-08', '2017-09', '2018-04-10', 
        '2018-04-11', '2018-04-16', '2018-05-03', '2018-04-14', '2018-04-15', '2017-01', '2017-02', '2017-03', '2017-04',
        '2017-05', '2017-06', '2017-07', '2018-05-24'
    ]




def get_req_tables(date_src):
    """
    Функция, генерирующая список архивированных и неархивированных таблиц из папки
    feed_validation_log
    :type date_src: string
    :rtype: list

    """
#интервал архивации
    INTERVAL = 2
# обработка даты запуска
# сначала строка преобразуется в datetime
# приводится к первому дню месяца и рассчитывается предыдущий месяц
    date_begin = datetime.strptime(date_src, '%Y-%m-%d')
    start_month = datetime(date_begin.year, date_begin.month, 01)
    prev_month = start_month - timedelta(days =1)

# рассчитывается месяц последней архивации
# рассчитывается последний день месяца последней архивации, а также дата
    max_archived_month = prev_month.month - INTERVAL
    max_archived_year = prev_month.year
    last_day_archived = calendar.monthrange(max_archived_year, max_archived_month)[1]
    last_date_archived = datetime(max_archived_year, max_archived_month, last_day_archived)

# формируется set из архивированных и неархивированных таблиц, затем они склеиваются

    start = datetime(2017, 1, 1)
    end = last_date_archived


    archived = set(date.strftime('%Y-%m-%d')[:7] for date in get_date_range(start, end))


    first_date_not_archived = last_date_archived + timedelta(days=1)
    not_archived = set(date.strftime('%Y-%m-%d') for date in get_date_range(first_date_not_archived, date_begin))

    req_tables = list(archived | not_archived)

    return req_tables


def get_date_range(start, end):

    date_generated = [start + timedelta(days=x) for x in range(0, (end-start).days + 1)]

    return date_generated

def compare_lists(src1, src2):
    """
    Функция для теста, проверяет равенство двух списков
    :type src1: list
    :type src2: list
    :rtype: Bool

    """
    if len(src1) != len(src2):
        return False

    for elem1 in src1:
        if elem1 in src2:
            continue
        else:
            return False
    return True


if __name__ == '__main__':

    print get_req_tables('2018-06-02')
    assert compare_lists(get_req_tables('2018-06-02'), LIST_FOR_TEST) == True
