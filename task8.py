n = int(input("input n "))
m = int(input("input m "))
k = int(input("input k "))
if m*n%k:
    print(f"{n} {m} {k} yes")
else:
    print(f"{n} {m} {k} no")
