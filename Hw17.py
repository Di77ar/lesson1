# Условия задачи
# Дана строка. Сохранить в ней только первые вхождения символов,
# удалив все остальные. Результат вывести в виде кортежа.
a= 'Hello my friends'
c=[]
for i in range(len(a)):
    if a[i] not in c:
        c.append(a[i])
print(tuple(c))