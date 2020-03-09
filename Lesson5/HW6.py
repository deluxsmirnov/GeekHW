my_dict = {}
with open('HW6.txt') as file:
    for i in file:
        name_lesson = i.split(':')[0]
        hour = i.split()[1:]
        my_dict[name_lesson] = 0
        for a in hour:
            my_dict[name_lesson] += int(a[:a.find('(')])
print(my_dict)
