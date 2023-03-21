# Формируется матрица F следующим образом: если в Е количество чисел, больших К в четных столбцах в области 2 больше,
# чем произведение чисел в нечетных строках в области 4, то поменять в С симметрично области 1 и 4 местами, 
# иначе С и В поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: К*(A*F)+ K*Fт. 
# Выводятся по мере формирования А, F и все матричные операции последовательно.
import random

K_test = 3 # Тестовые данные
N_test = 10
E_test = [
    [9, 5, 1, 6, -3],
    [1, 6, -5, -1, -4],
    [-8, -2, -3, 7, 9],
    [-7, 6, 0, -8, 4],
    [-3, -9, -4, -1, -5]]

B_test = [
    [-8, -7, 1, 1, 10],
    [-1, 10, 5, -10, -6],
    [1, 8, 0, 9, 5],
    [2, 1, -8, -5, -1],
    [-3, -6, 9, 7, -6]]

C_test = [
    [5, 7, -1, -7, -6],
    [2, 3, 10, -8, 4],
    [-4, -7, -10, -4, -5],
    [0, 9, -8, 9, -4],
    [10, -8, -10, -1, 8]]

D_test = [
    [-7, 1, 7, 8, -3],
    [-1, 6, -5, 2, 2],
    [-4, -2, 1, -2, -2],
    [2, -3, 0, -7, -1],
    [-8, -10, 3, 0, -5]]

print('Использовать тестовые данные или случайные?')
choice = input('Ваш выбор (1 - тестовые данные, 2 - случайные, q-выход): ')

if choice == '1':
    K = K_test
    N = N_test
    B, C, D, E = B_test, C_test, D_test, E_test
    n = N // 2  # Размерность матриц B, C, D, E (n x n)

if choice == '2': # Генерация случайных данных
    K = input("Введите число К=")
    N = input("Введите число N=")
    if (N % 2 != 0) or ((N / 2) % 2 == 0) or ((N / 2) < 3):
        print(
            'Ошибка в исходных данных. Число N должно быть четным и таким, чтобы число N/2 было нечетным и больше или равно 3')
        exit()

    B, C, D, E = [], [], [], []
    n = N // 2  # Размерность матриц B, C, D, E (n x n)
    for row in range(n):
        row_b, row_c, row_d, row_e = [], [], [], []
        for col in range(n):
            row_b.append(random.randint(-10, 10))
            row_c.append(random.randint(-10, 10))
            row_d.append(random.randint(-10, 10))
            row_e.append(random.randint(-10, 10))
        B.append(row_b)
        C.append(row_c)
        D.append(row_d)
        E.append(row_e)

if choice == 'q':
    exit()

A = []
for row in range(n):
    A.append(E[row] + B[row])

for row in range(n):
    A.append(D[row] + C[row])

# печатаем матрицы E, B, C, D, A
print('Матрица E:')
for row in range(n):
    print(E[row])

print('Матрица B:')
for row in range(n):
    print(B[row])

print('Матрица C:')
for row in range(n):
    print(C[row])

print('Матрица D:')
for row in range(n):
    print(D[row])

print('Матрица A:')
for row in range(N):
    print(A[row])

# Считаем произведение чисел в нечетных строках в области 4 в матрице E
x = 1
for row in range(1, n):
    if row <= n // 2:
        end_col = row
    else:
        end_col = n - 1 - row
    for col in range(0, end_col+1):
        if (row + 1) % 2 == 1:
            x = x * E[row][col]
print(f'Произведение чисел в нечетных строках в области 4 в матрице E: {x}')

# Считаем количество чисел, больших К в четных столбцах в области 2 в матрице E
count_more_K = 0
for row in range(1, n):
    if row <= n // 2:
        begin_col = n - 1 - row
    else:
        begin_col = row
    for col in range(begin_col, n):
        if (col + 1) % 2 == 0:  # Нумерация столбцов начинается с 1
            if E[row][col] > K:
                count_more_K += 1  # Увеличиваем счетчик
print(f'Количество чисел, больших К в четных столбцах в области 2 в матрице E: {count_more_K}')

F = [] # Создаём матрицу F следующим образом
if count_more_K > x: # Если в Е количество чисел, больших К в четных столбцах в области 2 больше, чем произведение чисел в нечетных строках в области 4,...
    C_F = C
    for row in range(1, n): #...то поменять в С симметрично области 1 и 4 местами,...
        if row <= n // 2:
            end_col = row
        else:
            end_col = n - 1 - row
        for col in range(0, end_col):
            C_F[row][col], C_F[col][row] = C_F[col][row], C_F[row][col]
    for row in range(n):
        F.append(E[row] + B[row])
    for row in range(n):
        F.append(D[row] + C_F[row])
else: # иначе С и В поменять местами несимметрично
    for row in range(n):
        F.append(E[row] + C[row])
    for row in range(n):
        F.append(D[row] + B[row])
print('Матрица F:')
for row in range(N):
    print(F[row])

A_and_F = []  # Умножаем матрицы A и F
for row in range(N):
    F_row = []
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += A[row][j] * F[j][i]
        F_row.append(sum)
    A_and_F.append(F_row)

print('Матрица A*F:')
for row in range(N):
    print(A_and_F[row])

A_and_F_and_K = [] # Умножаем произведение матриц A и F на константу K
for row in range(N):
    cur_row = []
    for col in range(N):
        cur_row.append(0)
    A_and_F_and_K.append(cur_row)  # формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам

for row in range(N):
    for col in range(N):
        A_and_F_and_K[row][col] = K * A_and_F[row][col]

print('Матрица F*A*K:')
for row in range(N):
    print(A_and_F_and_K[row])

F_transpose = [] # Транспонируем матрицу F
for row in range(N):
    F_transpose_row = []
    for col in range(N):
        F_transpose_row.append(F[col][row])
    F_transpose.append(F_transpose_row)

print('Транспонированная матрица F:')
for row in range(N):
    print(F_transpose[row])

F_transpose_and_K = [] # Умножаем транспонированную матрицу F на константу K
for row in range(N):
    cur_row = []
    for col in range(N):
        cur_row.append(0)
    F_transpose_and_K.append(cur_row)  # Формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам

for row in range(N):
    for col in range(N):
        F_transpose_and_K[row][col] = K * F_transpose[row][col]

print('Транспонированная матрица F, умноженная на K:')
for row in range(N):
    print(F_transpose_and_K[row])


result_matrix = []  # Результирующая матрица(сумма A*F*K и Fт*K)
for row in range(N):  # Формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам
    cur_row = []
    for col in range(N):
        cur_row.append(0)
    result_matrix.append(cur_row)

for row in range(N):
    for col in range(N):
        result_matrix[row][col] = A_and_F_and_K[row][col] + F_transpose_and_K[row][col]

print('Результат:')
for row in range(N):
    print(result_matrix[row])