my_list = [123, 25.25, "string", True, ("one", "two"), ["list_to_list"], ('tuples'), {"set_in_list", 123, 123, 332}, {"signaling" : "SS7", "signaling_2": "PRI"}]
i = 0
while i < len(my_list):
    print(f'{my_list[i]} {"-" * 10} {type(my_list[i])}')
    i += 1




