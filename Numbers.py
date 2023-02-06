#Для чтения данных из файла
exodus = open('numbers.txt')
Numbers = {}
b = 0
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
for i in exodus:
    if is_number(i) == False:
        continue
    else:
        Numbers[b] = list(i)
        b+=1
for n in Numbers:
    while Numbers[n][0] == '0':
        Numbers[n].remove('0')
    for k in Numbers[n]:
        print(k)

#Для ввода данных с клавиатуры
F_end, i = 0, 0
Numbers = {}
while F_end < 3:
    Number = input("Введите число К=")
    if int(Number) == 0:
        F_end += 1
    else:
        F_end = 0
        Numbers[i] = list(Number)
        i += 1
for n in Numbers:
    while Numbers[n][0] == '0':
        Numbers[n].remove('0')
    for k in Numbers[n]:
        print(k)
    print('')
