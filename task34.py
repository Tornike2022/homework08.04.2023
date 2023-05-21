def vinnys_chant(chant):
    chant = chant.split()
    list = []
    for word in chant:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        list.append(result)
    return len(list) == list.count(list[0])

print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
str = input()
if vinnys_chant(str):
    print('Парам пам-пам')
else:
    print('Пам парам')