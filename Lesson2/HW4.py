input_word = input("Введите слова через пробел ")
input_word = input_word.split()
for i in enumerate(input_word, 1):
    print(i[0], i[1][:10])

