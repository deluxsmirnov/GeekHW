from itertools import cycle, count


for el in count(7):
    print(el)

some_list = [12, 33, 455, 12, 312, 312, 3, 123, 123, 123, 345]


for i in cycle(some_list):
    print(i)
