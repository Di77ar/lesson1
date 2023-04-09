# Условия задач
# 1. Дано 2 множества, содержащих названия IT-компаний. Найти только те компании, которые содержатся в обоих множествах.
name1={'Ntt','ibm','microsoft','apple','ipam'}
name2={'ipam','overone','mac','ibm'}
a=[]
for i in list(name1):

    if i not in name2:
        continue
    else:
        a.append(i)
print(set(a))

# 2. Сгенерировать n множеств. Вывести множества кратные трём и не входящие в первое множество.

import random
n=int(input('введите количество множеств: '))
set1=[]
for i in range(n):
    s=[]
    for j in range(10):
        s.append(random.randint(1,100))

    set1.append(s)
print(set1)
res=set(set1[0])
print(res)
rec=set()
print(type(rec))
r=[]
l=1
while n!=0:
    for j in set1[1::]:

        for i in j:
            # print(i)
            if i%3==0 and i not in set1[0]:
                print('i='+str(i))
                r.append(i)

    n=l-1
print(set(r))