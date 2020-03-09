with open('HW3.txt', 'r', encoding='utf-8') as file:
    perevod_list = file.read().split("\n")
    perevod_list.remove('')
    all_zp = []
    less_zp = []
    for i in perevod_list:
        i = i.split()
        if int(i[2]) < 20000:
            less_zp.append(i[0])
        all_zp.append(int(i[2]))
    less_zp_stroka = ' '.join(less_zp)

    print(f'Зарплата меньше 20000 у сотрудника(ов) {less_zp_stroka} средняя величина доходов равна {sum(all_zp)/ len(all_zp)}')
