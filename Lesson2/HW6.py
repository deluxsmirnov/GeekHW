print('Необходимо ввести количество вводимых товаров, название товара, цену и кол-во товара на складе')
quantity = int(input('Введите сколько какое кол-во товаров будете вводить '))
i = 0
spisok_product = []
common = []
while i < quantity:
    product = input('Введите название товара ')
    price = input('Укажите стоимость товара ')
    quantity_product = input('Введите кол-во на складе ')
    my_dict = dict([('название', product),('цена', price),('количество', quantity_product),('ед', 'шт')])
    spisok_product.append(my_dict)
    i += 1
for i in enumerate(spisok_product, 1):
    common.append(i)
print(common)
print('\nИтого на складе есть\n')
j = 0
spisok_prod = []
spisok_money = []
spisok_ed = []
while j < len(spisok_product):
    spisok_prod.append(spisok_product[j]['название'])
    spisok_money.append(spisok_product[j]['цена'])
    spisok_ed.append(spisok_product[j]['количество'])
    j += 1
new_dict = dict([('название', spisok_prod),('цена', spisok_money),('количество', spisok_ed),('ед', ['шт.'])])
print(new_dict)


