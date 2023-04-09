# вводится число n найти все простые числа в диапазоне от 1 до n
chislo=int(input('введите число: '))
for i in range(1,chislo):
    summ=0
    for j in range(1,i+1):

        if i%j==0:
            summ+=j
    if i+1==summ:
        print(f'число  {i} простое')