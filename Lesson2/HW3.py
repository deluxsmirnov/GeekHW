from_user = int(input("Введите месяц в виде целого числа от 1 до 12 "))
mounth_dict = {
    1: ("Январь", "Зима"),
    2: ("Февраль", "Зима"),
    3: ("Март", "Весна"),
    4: ("Апрель", "Весна"),
    5: ("Май", "Весна"),
    6: ("Июнь", "Лето"),
    7: ("Июль", "Лето"),
    8: ("Август", "Лето"),
    9: ("Сентябрь", "Весна"),
    10: ("Октябрь", "Весна"),
    11: ("Ноябрь", "Весна"),
    12: ("Декабрь", "Зима")
}
print (f'Вы выбрали месяц {mounth_dict[from_user][0]} и это {mounth_dict[from_user][1]}')

from_user = int(input("Введите месяц в виде целого числа от 1 до 12 "))
list_mounth = [("Январь", "Зима"),("Февраль", "Зима"),("Март", "Весна"),("Апрель", "Весна"),("Май", "Весна"),
               ("Июнь", "Лето"),("Июль", "Лето"),("Август", "Лето"),("Сентябрь", "Весна"),("Октябрь", "Весна"),
               ("Ноябрь", "Весна"),("Декабрь", "Зима")]
print (f'Вы выбрали месяц {mounth_dict[from_user][0]} и это {mounth_dict[from_user][1]}')
