print('Необходимо вводить числа через пробел, будет посчитана сумма, после ввода нажмите Enter, для выхода можете ввести цифры и в конце Q')
def sum_num():
    b = []
    while True:
        num_from_user = input("Введите целые числа через пробел и нажмите Enter ").split()
        if "Q" in num_from_user:
            num_from_user.remove('Q')
            for i in num_from_user:
                b.append(int(i))
            break
        else:
            for i in num_from_user:
                b.append(int(i))
        print(sum(b))
    return sum(b)
print(sum_num())


