def print_operation_table(operation, num_rows=6, num_columns=6):
    n = [[operation(i, f) for f in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in n:
        print(*[f"{x:>3}" for x in i])

print_operation_table(lambda x, y: x * y)