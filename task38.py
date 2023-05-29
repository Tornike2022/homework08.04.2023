menu = ["first_name", "last_name", "number"]
collect = {}
d=1
with open ("phonebook_file.txt", "r", encoding="utf8") as file:
    for l in file:
        l=l.replace("\n", '')
        collect[d]=list(l.split(";"))
        d=d+1
dictPhone = collect
path = "phonebook_file.txt"
def FindNumber(dict):
    find = str(input("ведите ваш запрос для поиска: "))
    for i in dict:
        for j in range(len(dict[i])):
            if find in dict[i][j]:
                print(dict[i])

def getPhone(dictP):
    for i in dictP:
        print(dictP[i])
def choice(n, dict):
    if n==1:
        getPhone(dict)
    if n==2:
        FindNumber(dict)
    if n==3:
        addPhone()
        getPhone(dict)
    if n ==4:
        Change_data(dict)
    if n==5:
        Delete_data(dict)

def addPhone():
    s=1
    save = list(input("input surname name and phone using shift: ").split())
    while True:
        if s in dictPhone:
            s=s+1
        else:
            dictPhone[s] = save
            break
def Delete_data(dict):
    print(dict)
    s = int(input('Input the record number to delete: '))
    if len(dict) < s:
            print("The record doesn't exist")
    else:
        del dict[s]
def Change_data(dict):
    print(dict)
    s = int(input('Input the record number to change: '))
    if len(dict) < s:
            print("The record doesn't exist")
    else:
        k = int(input('Change: Surname(0) Name(1) Phone Number(2): '))
        dict[s][k] = input('Input the new record: ')
print("Hello")
print("chose what to do with the phonebook from 1 to 3: ")
print("1 - show the phonebook, 2 - find the record, 3 - add data to the phonebook, 4 - edit data, 5 -delete data")

n=int(input())
choice(n,dictPhone)
with open ("phonebook_file.txt", "w", encoding="utf8") as file:
    for k in dictPhone:
        file.write(f'{dictPhone[k][0]};{dictPhone[k][1]};{dictPhone[k][2]}\n')
collect = {}
d=1
with open ("phonebook_file.txt", "r", encoding="utf8") as file:
    for l in file:
        l=l.replace("\n", '')
        collect[d]=list(l.split(";"))
        d=d+1
print(collect)