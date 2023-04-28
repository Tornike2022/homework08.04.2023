def sum(a, b):
    if b == 0:
        return a
    elif b > 0:
        return sum(a+1, b-1)
    else:
        return sum(a-1, b+1)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("Суммой двух чисел будет: ", sum(a, b))