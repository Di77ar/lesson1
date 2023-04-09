# в файле хранятся строки посчитать длину каждой
# with open("practFile.txt", "w") as f:
#
#     for i in range(5):
#         f.write(input('введите текст: '))
#         f.write('\n')
f=open('practFile.txt','r')
j=f.readlines()
f.close()
for i in j:
    print(len(i))