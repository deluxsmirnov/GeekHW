from sys import argv

the_prize = 5000

script_name, work_hour, stavka = argv

print(f'Вы отработали {work_hour} часа(ов)')
print(f'Ставка в час составляет {stavka} у.е.')
print(f'Ваша зароботная плата будет {int(float(work_hour) * float(stavka) + the_prize)} у.е. с учётом премии {the_prize} у.е.')
