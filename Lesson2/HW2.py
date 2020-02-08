input_user = input("Введите элементы списка через пробел ")
spisok = input_user.split()
i = 0
if len(spisok) % 2 == 0:
    while i < len(spisok):
        spisok[i],spisok[i+1] = spisok[i+1],spisok[i]
        i +=2
    print(spisok)
elif len(spisok) % 2 != 0:
    a = spisok[-1]
    spisok.pop()
    while i < len(spisok):
        spisok[i],spisok[i+1] = spisok[i+1],spisok[i]
        i +=2
    spisok.append(a)
    print(spisok)

input_user = input("Введите элементы списка через пробел ")
spisok = input_user.split()
i = 0
while i < len(spisok) - 1:
    spisok[i],spisok[i+1] = spisok[i+1],spisok[i]
    i += 2
print(spisok)
