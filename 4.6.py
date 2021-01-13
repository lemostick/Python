from itertools import count
from itertools import cycle

# бесконечный итератор, генерирующий целые числа, начиная с указанного

print ('Внимание, программа предусматривает бесконечный цикл, останавливается Ctrl+C!')
for el in count(int(input('Введите стартовое число: '))):
    print(el) 

