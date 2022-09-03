def game_start(up, down):
    import random
    count = 0
    
    up, down = int(up), int(down)
    if up > down:
        up, down = down, up
        
    num = random.randint(up, down)
    while True:
        put = input()
        
        if put.isdigit() == False:
            print()
            print('Мы же гадаем целые числа.')
            continue
        
            
        if int(put) > num:     
            print('Число меньше.')
            count += 1
            print('Количество попыток:', count)
            
        elif int(put) < num:
            print('Число больше.')
            count += 1
            print('Количество попыток:', count)
            
        elif int(put) == num:
            print()
            print('О да, ты угадал. Это число =', num)
            print('Поздравляю, ты смог угадать число за столько попыток: ', count)
            break
    print()
    return('Сыграем ещё?')
