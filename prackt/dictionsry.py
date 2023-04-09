dict1=dict(str1='hello',str2='world')
print(dict1)
dict2={'chislo1':1,'chislo2':2,'chislo3':[1,5,4]}
print(dict2)
for i in dict2.values():
    print(i)
for i in dict2.keys():
    print(i)
dict2={'chislo':[1,45,4,84,6]}
for i,j in dict2.items():
    print(i,j[1])
