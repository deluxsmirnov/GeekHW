with open('First.txt', 'w', encoding='utf-8') as homedz:
    from_user = []
    print('Необходимо вводить какие либо слова или числа и всё запишется в файлик. Если устали вводить, просто нажмите Enter')
    while True:
        vvod = input("Введи, что-нибудь: ")
        if vvod == '':
            break
        from_user.append(vvod + '\n')
    homedz.writelines(from_user)

print(from_user)
