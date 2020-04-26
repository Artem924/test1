'''
Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
'''

a = [i for i in range(100, 1001) if i % 2 == 0]
print(a)
from functools import reduce
def my_funk(a):
    result = reduce((lambda x, y: x * y), a)
    return result
print(my_funk(a))
