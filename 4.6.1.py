from itertools import count
from itertools import cycle
# бесконечный итератор, повторяющий элементы некоторого списка

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el)