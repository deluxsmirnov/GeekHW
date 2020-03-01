def my_funk(x, y):
    return x ** abs(y)

print(my_funk(2, -3))

def my_funk_2(x, y):
    a = [x]
    for i in range(abs(y)-1):
        a.append(a[i] * x)
    return max(a)

print(my_funk_2(2, -3))
