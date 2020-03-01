from math import factorial

def fibo_gen(nums):
    for i in range(1, nums):
        if i >15:
            break
        yield factorial(i)

for k in fibo_gen(20):
    print(k)


