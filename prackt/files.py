# .txt
f=open("exemple.txt",'r')
# f.write('hello world!\n hello')# запись
# f.writelines(['\njsnckjncsk','jcbsjcbkja','ajncskjasjcbkj'])#запись в виде списка записывает строку
# print(f.read(10)) #читает из файла первые 10 знаков
# print(f.readline())# читает первую строку
# print(f.readlines())# читает файл в виде списка


with open('exemple.txt','a') as f:#позволяет создавать файл без использования closed
    f.write('\njshkjaskjas')
