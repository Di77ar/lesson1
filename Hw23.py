# Условие задачи
# Написать функцию, которая заполняет массив случайными числами в диапазоне, указанном пользователем.
# Функция должна принимать два аргумента - начало диапазона и его конец, при этом ничего не возвращать.
# Вывод значений элементов массива должен происходить в основной ветке программы.

import random
def massiVe(a,b):
    c=[]
    for i in range(10):
        c.append(random.randint(a,b))
    return (c)
print(massiVe(int(input('eвведите нижнее значение диапазона: ')),int(input('введите верхнее значение диапазона: '))))