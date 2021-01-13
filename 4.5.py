import functools
import math
import random
def my_func(num1, num2):
    return num1 * num2

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {functools.reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')