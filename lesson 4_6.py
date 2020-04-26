'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from itertools import count
for i in count(54):
    print(i)

from itertools import cycle
a = ["abs", "cda", "333"]
for i in cycle(a[1]):
    print(i)
