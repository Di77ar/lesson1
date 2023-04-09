# Условия задач
# 1. Найти максимальный элемент диагонали матрицы.

matrix = [[10, 11, 12, 13],
          [14, 15, 16, 17],
          [18, 19, 20, 21]]
n = len(matrix)
m = len(matrix[0])
print(n)
print(m)
print('Матрица:')
for i in matrix:
    print(i)
s=[]
for i in range(n):

    for j in range(m):
        if i == j:
            a=(matrix[i][j])
            s.append(a)
print(max(s))


# 2. Вычислить количество отрицательных элементов под главной диагональю матрицы.
import random
matrix = [[10, 11, 12, 13],
          [14, 15, 16, 17],
          [18, -19, 20, 21]]
matrix1=int(input('введите число строк'))
matrix2=int(input('введите количество столбцов'))
s=[]
for i in range(matrix1):
    s1=[]
    for j in range(matrix2):
        a=random.randint(-100,100)
        s1.append(a)
    s.append(s1)

print(s)
for i in s:
    print(i)

n = len(s)
m = len(s[0])


s3=[]
for i in range(n):
    for j in range(m):
        if i > j:
            a=(s[i][j])
            s3.append(a)
print(s3)
k=0
for i in s3:
    if i<0:
        k+=1
print(f'количество отрицательных элементов {k}')