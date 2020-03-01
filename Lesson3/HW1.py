print('Необходимо ввести целое число, если вводите дробное, оно округлится до целого')
num_1 = input('Введите число ')
num_2 = input('Введите число ')
def division (x, y):
    try:
        k = float(x) / float(y)
        return round(k)
    except ZeroDivisionError:
        print('На ноль делить нельзя, перезапусти программу')

print(division(num_1, num_2))
