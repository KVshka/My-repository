# Натуральные числа, начинающиеся с не менее чем 3 нулей. Вывести числа без незначащих нулей. Список используемых цифр вывести прописью.
import re # импорт библиотеки
Int = {'0':'ноль', '1':'один', '2':'два', '3':'три', '4':'четыре', '5':'пять', '6':'шесть', '7':'семь', '8':'восемь', '9':'девять'} # словарь с ключами-цифрами и их прописями
is_num = False # по умолчанию в файле нет чисел, соответствующих условию
number = "" # буфер ответа для цифр
string = "" # буфер ответа 
with open('numbers.txt', 'r') as exodus: # открываем файл
    while True:
        a = exodus.readline().split() # читаем строку
        if not a: # если файл пустой
            print("Файл *.txt в директории проекта кончился")
            break
        for i in a: # обрабатываем элементы строки
            res = re.findall(r'0*', i) # ищем последовательность нулей
            if len(res[0]) >= 3: # если выполняется условие задачи
                is_num = True # в файле есть хотя бы одно число, соответствующее условию
                b = list(i) # разбиваем строку с числом на символы
                while b[0] == '0': # удаляем незначащие нули
                    b.remove('0')
                for j in b:
                    number += j # добавляем цифру в буфер ответа
                    string = string + Int[j] + ' ' # добавляем пропись цифры в буфер ответа
                print(number + ' ' + string) # выводим ответ
                number = "" # возвращаем значения буферов ответа по умолчанию
                string = ""
    if is_num == False: # если нет чисел, соответствующих условию
        print("В файле нет чисел, соответствующих условию")