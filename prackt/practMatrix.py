# пользователь вводит  числовую матрицу n на m Найдите сумму каждой строки

n= int(input('введите число строк'))
m = int(input('введите число столбцев'))
import random
matrix=[]
for i in range(n):
    list1=[]
    for j in range(m):
        a=random.randint(-10,100)
        print(a)
        list1.append(a)
    matrix.append(list1)
for i in matrix:
    print(i)
for i in matrix:
    print(sum(i))