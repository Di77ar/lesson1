# Условие задачи
# В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество
# символов и слов в ней.

f=open('pracktFile.txt','r')
file=f.readlines()
f.close()
a=[]
for i in file:
    j=i.replace('\n','')
    a.append(i.replace('\n',''))
print(f'количество строк ровняется {len(a)}')
s=len(a)
q=0
while s!=0:
    i=(a[q])
    simbol = 0
    word=0
    for j in i.split(' '):
        word+=1
    print(f'длинна {q+1} строки равна {len(i)}, количество слов = {word}')
    q+=1
    s-=1