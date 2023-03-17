# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и
# столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов
# идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией
# называется любая операция, у которой ровно два аргумента, как, например, у
# операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

table_rows = int(input('Введите первое число (строки): '))                # простое решение через функцию и цикл
table_columns = int(input('Введите второе число (колонки): '))
action = input('Введите действие (+ - * /): ')
def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, table_rows + 1):
        for j in range(1, table_columns + 1):
            if action == '+':
                print((i + j), end='\t')
            elif action == '-':
                print((i - j), end='\t')
            elif action == '*':
                print((i * j), end='\t')
            elif action == '/':
                print(round((i / j), 4), end='\t')
        print()
print_operation_table(action, table_rows, table_columns)


# def print_operation_table(operation):                                    # решение через сложную функцию и цикл
#     table_rows = int(input("Введите количество строк: "))
#     table_colums = int(input("Введите столбцов: "))
#     table = list()
#     i, j, count = 0, 0, 0
#     while i < table_rows:
#         i += 1
#         while j < table_colums:
#             j += 1
#             table.append(operation(i, j))
#         j = 0
#     for i in table:
#         print(round(i, 4), end='\t')
#         count += 1
#         if count == table_rows:
#             print()
#             count = 0
# action = input('Введите действие (+ - * /): ')
# if action == '+':
#     print_operation_table(lambda x, y: x + y)
# elif action == '-':
#     print_operation_table(lambda x, y: x - y)
# elif action == '*':
#     print_operation_table(lambda x, y: x * y)
# elif action == '/':
#     print_operation_table(lambda x, y: x / y)
