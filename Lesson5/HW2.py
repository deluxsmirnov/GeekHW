file = open('HW2.txt', 'r', encoding='utf-8')
count = 0
for i in file:
    count += 1
    word = len([len(k) for k in i.split()])
    print(f'Кол-во слов в {count} строке {word}')
print(f'Количество строк записано в файле {count}')
file.close()
