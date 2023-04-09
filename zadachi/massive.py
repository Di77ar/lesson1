listA=[]
for i in range(10):
    listA.append(i)
print(listA)
listB=[]
for i in range(10):
    listB.append([1,2,3,4])
print(listB)
n=int(input('enter cifra strok:'))
m=int(input('enter cifra ctolbcov:'))
listC=[]
for i in range(n):
    listC1=[]
    for j in range(m):
        a=int(input())
        listC1.append(a)
    listC.append(listC1)
print(listC)
for i in listC:
    print(i)