def game_start(up, down):
    import random
    
    count = 0                                                           #Счётчик попыток
    
    up, down = int(up), int(down)                                       #Устанавливаем правельные границы (иначе вылет функции random на 10 -ой строчке)
    if up > down:
        up, down = down, up
        
    num = random.randint(up, down)
    
    print()
    print('Окей, теперь попробуй угадать число. Введи какое-нибудь.')
    
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
            count += 1
            print('Поздравляю, ты смог угадать число за столько попыток: ', count)
            break
    print()
    return('Сыграем ещё?')
