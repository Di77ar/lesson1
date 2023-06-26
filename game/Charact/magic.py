def maGician():
    sUm3 = None
    sUm = 4

    while sUm3 != '0':
        a = int(input("forse:"))
        if a > sUm:
            print('у вас нет столько очков')
            continue
        sUm1 = sUm - a
        if sUm1 == 0:
            break
        print(f'у вас осталось {sUm1} очков')
        b = int(input("hitpoint:"))
        if b > sUm1:
            print('у вас нет столько очков')
            continue
        sUm2 = sUm1 - b
        print(f'у вас осталось {sUm2} очков')
        if sUm2 == 0:
            break
        c = int(input("mana:"))
        if c > sUm2:
            print('у вас нет столько очков')
            continue
        sUm3 = sUm2 - c
        print('спасибо!')
        if sUm3 == 0:
            break
    chAract={'forse': a,'hitpoint':b,'mana':c}
    print(f'характеристики вашего героя \'класс маг\' {chAract}')
    return
