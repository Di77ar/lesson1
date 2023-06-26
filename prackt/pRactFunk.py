# # Написать функцию которая генерирует словарь, где ключ это буква строки, а значение это число, сколько раз повторяется
# # данная буква в этой строке
# # строку вводит пользователь
#
# str=input('asd')
# print(str)
# def gen_dict():
#     dict1={}
#     for i in str:
#         dict1[i]=str.count(i)
#     return dict1
# print(gen_dict())
# 2. реализовать калькулятор где операции это функуии

def pLus(a,b):
    c=a+b
    return(c)

def miNus(a,b):
    c=a-b
    return(c)

def umn(a,b):
    return a*b
def del1(a,b):
    return a/b
while True:
    chislo1 = int(input('введите первое число'))
    operator1 = input('введите оператор')
    chislo2 = int(input('введите второе число'))
    if operator1=='+':
        print(pLus(chislo1,chislo2))
    elif operator1=='-':
        print(miNus(chislo1, chislo2))
    elif operator1=='*':
        print(umn(chislo1, chislo2))
    elif operator1=='/':
        print(pLus(chislo1, chislo2))
    elif operator1=='0':
        break