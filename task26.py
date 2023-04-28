def in_power_of_recursive(a, b):
    if (b == 1):
        return (a)
    if (b!=1):
        return (a*in_power_of_recursive(a, b-1))

a = int(input("введите число "))
b = int(input("в какую степень возвести число а? "))
print(f"число {a} в степени {b} это {in_power_of_recursive(a, b-1)}")