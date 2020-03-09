dict_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('HW4_1.txt', 'w', encoding='utf-8') as new:
    with open('HW4.txt', 'r') as file:
        read_file = file.read().split("\n")
        read_file.remove('')
        for i in read_file:
            i = i.split()
            print(dict_num[i[0]] + ' эквивалент ' + i[2])
            new.writelines(dict_num[i[0]] + ' эквивалент ' + i[2] + "\n")
