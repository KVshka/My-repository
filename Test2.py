Buffer_len = 1 # размер буфера чтения
Int = {'0':'ноль', '1':'один', '2':'два', '3':'три', '4':'четыре', '5':'пять', '6':'шесть', '7':'семь', '8':'восемь', '9':'девять'} # словарь с ключами-цифрами и их прописями
is_3_0 = False # трёх нулей в числе нет
check = False # флаг опущен
is_num = False # по умолчанию в файле нет чисел, соответствующих условию
number = "" # буфер ответа для цифр
string = "" # буфер ответа 
with open('numbers.txt', 'r') as exodus: # открываем файл
    buffer = exodus.read(3) # читаем первый блок
    if not buffer: # если файл пустой
        print("Выбранный файл пустой. Добавьте не пустой файл в директорию или переименуйте существующий *.txt файл")
    while buffer: # пока файл не пустой
        if buffer == '000':
            is_3_0 = True # в начале числа есть три нуля
            buffer = exodus.read(Buffer_len) # читаем и обрабатываем следующий блок
            continue
        if buffer.isdigit() == True: # если блок содержит цифру
            if is_3_0 == True and ((buffer == '0' and check == True) or buffer != '0'): # если число соответствует условию
                number += buffer # добавляем цифру к строке ответа
                string = string + Int[buffer] + " " # добавляем пропись цифры к строке ответа
                check = True # поднимаем флаг
        else:
            is_3_0 = False
        if buffer == ' ':
            if check == True: # попадает под условие
                is_num = True # в файле есть хотя бы одно число, соответствующее условию
                print(number + ' ' + string) # выводим ответ
                check = False # опускаем флаг
                is_3_0 = False 
            number = "" # возвращаем значения буферов ответа по умолчанию
            string = ""
            buffer = exodus.read(3) # читаем следующий блок и обрабатываем его
            continue
        buffer = exodus.read(Buffer_len)
    if check == True: # проверяем, поднят ли флаг
        print(number + ' ' + string) # выводим последний ответ, если он есть
    if buffer and is_num == False: # если нет чисел, соответствующих условию
        print("В файле нет чисел, соответствующих условию")
