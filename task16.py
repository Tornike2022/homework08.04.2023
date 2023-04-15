N = int(input("Please input the len of the list of digits "))
A = []

for i in range(1, N+1):
    A.append(i)

print(*A)

X = int(input("Please input one digit from the list N "))
print(A.count(X))