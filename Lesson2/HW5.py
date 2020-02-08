sp = [7, 5, 3, 3, 2]
from_user = int(input(f'Есть список рейтинга {sp}, тебе необходимо ввести любое натуральное число.\nПрограмма определит куда вставить его - '))
if from_user in sp:
    sp.insert(sp.index(from_user) + sp.count(from_user), from_user)
else:
    if from_user > max(sp):
        sp.insert(0, from_user)
    if from_user < min(sp):
        sp.insert(len(sp), from_user)
    if from_user < max(sp) and from_user > min(sp):
        i = 0
        while from_user < sp[i]:
            i += 1
        sp.insert(i, from_user)
print(sp)
