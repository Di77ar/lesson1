# Домашнее задание :)
# Условия задач
# 1. Придумать и обработать исключения на TypeError и ValueError.
# 2. Известны год, номер месяца и день рождения человека, а также
# день, год и номер месяца сегодняшнего дня. Определите возраст человека (число полных лет).
try:
    import datetime
    dayH=int(input('введите день рождения '))
    mountH=int(input('введите месяц рождения '))
    yearH=int(input('введите год рождения '))
    dateNowday = 21
    dateNowmount = 3
    dateNowyear = 2023
    date1 = datetime.date(yearH,mountH,dayH)
    date2 = datetime.date(dateNowyear,dateNowmount,dateNowday)
    oldday = (date2-date1)/365.25
    print(f"ваш возраст {oldday.days} лет")

except ValueError:
    print('Внимательнее')
except TypeError:
    print('Чтото пошло не так')

try:
    import datetime
    yearOld=int(input('введите год рождения'))
    monthOld=int(input('введите месяц рождения'))
    dayOld=int(input('введите день рождения'))
    a=datetime.date(year=yearOld, month=monthOld, day=dayOld)
    b=datetime.datetime.now().date()
    c=(b-a)
    s=c/365
    print(f'ваш возраст {s.days} лет')
except ValueError:
    print('Внимательнее')
except TypeError:
    print('Чтото пошло не так')

