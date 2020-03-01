spisok = [23, 33, 3212, 23, 32333, 12, 2233, 33, 323, 445, 656, 666, 455, 555, 234, 32333]

generator = [i for i in spisok if spisok.count(i) == 1]

print(generator)
