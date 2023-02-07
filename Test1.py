exodus = open('numbers.txt')
Int = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in exodus:
    a = list(i)
    while a[0] == '0':
        a.remove('0')
    for k in a:
        for b in Int:
            if k == b:
                print(k)
    print('')