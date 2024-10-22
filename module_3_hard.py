def calculate_structure_sum(args):                      # Создаём функцию
    total_sum = 0                                       # Обьявляем переменную для суммирования цифр и строк

    if isinstance(args, int):                           # Если нашли целое число
        return args                                     # Выходим из функции возвращая целое число
    elif isinstance(args, str):                         # Если нашли строку
        return len(args)                                # Выходим из функции возвращая количество элементов
    elif isinstance(args, (list, tuple, set)):          # Если нашли список, кортеж, набор
        for i in args:                                  # Перебираем их
            total_sum += calculate_structure_sum(i)     # Плюсуем количество символов и числа рекурсивно
    else:                                               # Иначе
        for i in args.values():                         # Перебираем значения словарей
            total_sum += calculate_structure_sum(i)     # Плюсуем значения словарей рекурсивно
        for i in args.keys():                           # Перебираем ключи словарей
            total_sum += calculate_structure_sum(i)     # Плюсуем их рекурсивно
    return total_sum                                    # Возвращаем сумму всех цифр и элементов строк


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
