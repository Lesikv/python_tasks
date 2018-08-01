#!usr/bin/env python
#coding: utf-8


def get_digit(src, num):
    """
    Функция, получающая k разряд числа в исходном массиве
    """
    return (src / 10**num) % 10

def get_max_digit(src):
    """
    Функция, возвращающая максимальный разряд числа
    """
    digit = 0
    while src > 0:
        digit += 1
        src /= 10
    return digit

def get_max_digit_in_arr(arr):
    max_digit = None
    for num in arr:
        cur_digit = get_max_digit(num)
        if cur_digit > max_digit:
            max_digit = cur_digit
    return max_digit



def get_digit_array(arr, num):
    """
    Функция, возвращающая массив из чисел k разряда элементов исходного массива
    """
    digits = []
    for number in arr:
        digit = get_digit(number, num)
        digits.append(digit)
    return digits

def count_digits(arr):
    """
    Функция, которая считает количество встречаемых чисел в k разряде
    """
    res = [0 for i in range(10)]
    for i in range(10):
        for elem in arr:
            if elem == i:
                res[i] += 1
    return res

def fill_array(arr):
    """
    Функция, которая генерирует массив с интервалами заполнения
    """
    res = [0 for i in range(10)]
    for i  in range(1, len(arr)):
        cnt_prev = arr[i-1]
        res[i] = res[i-1] + cnt_prev
    return res

def fill_sorted_array(interval_arr, src_array, k):
    sorted_res = [0 for i in range(len(src_array))]
    for i in range(len(src_array)):
        digit = get_digit(src_array[i], k)
        res_idx = interval_arr[digit]
        sorted_res[res_idx] = src_array[i]
        interval_arr[digit] += 1

    return sorted_res

def radix_sort(arr):
    cur_arr = arr
    for k in range(get_max_digit_in_arr(arr)):
        cnt_arr = count_digits(get_digit_array(arr, k))
        interval_arr = fill_array(cnt_arr)
        cur_arr = fill_sorted_array(interval_arr, cur_arr, k)
    return cur_arr





if __name__ == '__main__':
    assert get_digit(458, 0) == 8
    assert get_digit_array([500, 012, 123, 456, 479], 2) == [5, 0, 1, 4, 4]
    assert count_digits(get_digit_array([500, 012, 123, 456, 479], 2)) == [1, 1, 0, 0, 2, 1, 0, 0, 0, 0]
    assert fill_array(count_digits(get_digit_array([500, 012, 123, 456, 479], 2))) == [0, 1, 2, 2, 2, 4, 5, 5, 5, 5]
    #print fill_sorted_array(fill_array(count_digits(get_digit_array([500, 012, 123, 456, 479], 2))), [500, 12, 123, 456, 479], 2)
    print radix_sort([500, 12, 123, 456, 479])
