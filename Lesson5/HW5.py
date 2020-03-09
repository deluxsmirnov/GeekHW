with open('HW5.txt', 'w') as file:
    file.writelines('22 33 44 55 66 77 88')

with open('HW5.txt', 'r') as file:
    new_spisok_num = []
    read_file = file.read().split()
    for i in read_file:
        num = int(i)
        new_spisok_num.append(num)
    var = ' '.join(read_file)
    print(f'В файле числа {var} сумма всех чисел равна = {sum(new_spisok_num)}')

