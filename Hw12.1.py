# Условие задач
# 1. Найти сумму и произведение цифр введённого трёхзначного натурального числа. Например, если
# введено число 325, то сумма его цифр равна 10 (3+2+5), а произведение - 30 (325).
#
try:
    chislo1=int(input('введите трехзначное число: '))

    if len(str(chislo1))==3:
        j=0
        k=1
        for i in str(chislo1):
            j+=int(i)
            k=k*int(i)
        print(f'сумма чисел равна - {j}')
        print(f'произведение чисел равно - {k}')
    else:
        print('вы ввели неверную длину числа')

except ValueError:
    print('только цифры')

# 2. Вывести на экран ряд натуральных чисел от минимума до максимума с шагом.
# Например, если минимум 10, максимум 35, шаг 5, то вывод должен быть таким: 10 15 20 25 30 35.
# Минимум, максимум и шаг указываются пользователем (считываются с клавиатуры).
try:
    chisloMin=int(input('введите минимальное натуральное число: '))
    chisloMax=int(input('введите максимальное натуральное число число: '))
    step=int(input('введите шаг: '))

    for i in range(chisloMin,chisloMax,step):
        print(i)
except ValueError:
    print('только натуральные числа, будьте внимательны')