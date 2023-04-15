N = int(input("Please input the len of the list of digits "))
A = []

for i in range(1, N+1):
    A.append(i)
X = int(input("Please input X digit "))
min = X - A[0]
index = 0
for i in range (1, N):
    count = abs(X-A[i])
    if count < min:
        min = count
        index = i
print(f"Digit {A[index]} is the closest to the {X}")