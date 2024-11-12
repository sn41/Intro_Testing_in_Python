# Создается переменная под названием total;
# Перебираются все значения в arg
#   и добавляются к total;
# Затем, по завершении итерации, результат возвращается.

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total