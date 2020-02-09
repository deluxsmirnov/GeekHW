def my_func(var_1, var_2, var_3):
    a = []
    for i in var_1,var_2,var_3:
        a.append(i)
    return sum(a) - min(a)


print(my_func(10, 110, 3))
