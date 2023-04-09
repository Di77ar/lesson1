# #на входе десятизначное число. посчитать сумму всех его цифр
# import random
# n= random.randint(1000000000,9999999999)
# print(n)
# summ=0
# for i in str(n):
#     print(i)
#     summ=summ+int(i)
# print(summ)

# пользователь вводит высоту треугольника необходимо построить прямоугольный треугольник

high=int(input('введите высоту треугольника: '))
for i in range(1,high+1):


    for j in range(i):
        print('*', end=' ')
    print()