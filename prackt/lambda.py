#
# def pLus(a,b):
#     c=a+b
#     return(c)
pLus=lambda a,b:a+b
# def miNus(a,b):
#     c=a-b
#     return(c)
miNus=lambda a,b:a-b
# def umn(a,b):
#     return a*b
umn=lambda a,b:a*b
# def del1(a,b):
#     return a/b
del1=lambda a,b:a/b
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