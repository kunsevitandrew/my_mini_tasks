# Optimal algorithm for splitting a number into digits

import time
import random

#
def time_of_func(func):
    def wrapper(*args, **kwargs):
        my_time = time.time()
        func(*args, **kwargs)
        my_time -= time.time()
        print(f"Lead time of func {func.__name__} is {abs(my_time)}")

    return wrapper


@time_of_func
def test_func(func):
    for i in range(10 ** 7):
        func(random.randint(100000, 999999), 6)


def split_number_1(numb, digs) -> bool:
    return sum(map(int, str(numb))) == digs


def split_number_2(numb, digs) -> bool:
    sum_of_numbers = 0
    for i in range(digs):
        sum_of_numbers += numb % 10
        numb //= 10

    return sum_of_numbers == digs


test_func(split_number_1)
test_func(split_number_2)
