num_list = [23, 44, 21, 23, 11, 44, 212, 444, 123, 3322]

new_num_list = [num_list[el] for el in range(1, len(num_list)) if num_list[el] > num_list[el-1]]

print(new_num_list)
