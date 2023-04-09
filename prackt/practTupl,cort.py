# пользователь вводит последовательность чисел строкой нужно вывести список и кортежс этими числами
# str1=input('введите числа разделенные пробелами')
# list1=str1.split(' ')
# print(list1)
# tuple1=tuple(str1.split(' '))
# print(tuple1)

# пользователь вводит список нужно оставить только уникальные элементы и отсортировать его

# n=input('введите данные через пробелом ')
# spisoc=set(n.split(' '))
# print(spisoc)
# spisoc1=list(spisoc)
# spisoc1.sort()
# print(spisoc1)

# ПОЛЬЗОВАТЕЛЬ ВВОДИТ СЛОВО. нужно перевести его с руского на английский. слова с переводом хранятся в словаре

slowar={'толкать':'push','стол':"table","кот":'cat'}
n=input('введите слово: ')

if n in slowar:
    for key in slowar.keys():

        if key==n:
            print(slowar[key])