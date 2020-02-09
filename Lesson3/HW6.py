def int_func(*args):
    """Получаем значение слов в виде кортежа, далее его приводим в список. Всё содержимое инденксируется
    нулевым значение, тогда всё содержимое извлекаем и снова приводим к списку, где каждый элемент
    индексируется по очередно. Далее всё проходим циклом и первую букву переводим в верхний регистр.
    Финальным этапом будет всё вывести в строкую
    """
    perevod_list = list(args)
    index_from_list = perevod_list[0]
    union = list(index_from_list.split())
    new_list = []
    for i in union:
        new_list.append(i.capitalize())
    return ' '.join(new_list)
print(int_func("ivan sergeevich kuzov love world"))
