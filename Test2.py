# Натуральные числа, начинающиеся с не менее чем 3 нулей. Вывести числа без незначащих нулей. Список используемых цифр вывести прописью.
Buffer_len = 1 # размер буфера чтения
Int = {'0':'ноль', '1':'один', '2':'два', '3':'три', '4':'четыре', '5':'пять', '6':'шесть', '7':'семь', '8':'восемь', '9':'девять'} # словарь с ключами-цифрами и их прописями
check = False # флаг опущен
is_num = False # по умолчанию в файле нет чисел, соответствующих условию
number = "" # буфер ответа для цифр
string = "" # буфер ответа 
counter = 0 # счётчик незначащих нулей в числе
with open('numbers.txt', 'r') as exodus: # открываем файл
    buffer = exodus.read(Buffer_len) # читаем первый блок
    if not buffer: # если файл пустой
        print("Выбранный файл пустой. Добавьте не пустой файл в директорию или переименуйте существующий *.txt файл")
    while buffer: # пока файл не пустой
        for k in Int.keys(): # перебираем ключи словаря
            if buffer == k: # если блок содержит цифру
                if buffer == '0': # если блок равен 0
                    if check == True: # если ноль значащий и выполняется условие задачи
                        number += buffer # добавляем цифру в буфер ответа
                        string = string + Int[buffer] + ' ' # добавляем пропись цифры в буфер ответа
                    else: # если ноль незначащий
                        counter += 1 # прибавляем единицу к счётчику нулей
                else: # если блок отличен от 0
                    if counter >= 3: # если выполняется условие задачи
                        check = True # поднимаем флаг (условие выполняется и все последующие нули в числе значащие)
                        is_num = True # в файле есть хотя бы одно число, соответствующее условию
                        number += buffer # добавляем цифру к строке ответа
                        string = string + Int[buffer] + ' ' # добавляем пропись цифры к строке ответа
                    else: # если не выполняется условие задачи
                        break # выходим из цикла
            elif buffer == ' ' and check == True: # если последовательность символов закончилась и попадает под условие
                print(number + ' ' + string) # выводим ответ
                number = "" # возвращаем значения буферов ответа по умолчанию
                string = ""
                counter = 0 # обнуляем счётчик незначащих нулей
                check = False # опускаем флаг
        buffer = exodus.read(Buffer_len) # читаем следующий блок
    if is_num == False: # если нет чисел, соответствующих условию
        print("В файле нет чисел, соответствующих условию")