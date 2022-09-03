from f_test_number import test_number
from f_game_start import game_start

while True:
    print()
    up = input('Введите верхний диапазон числа = ')
    down = input('Введите нижний диапазон числа = ')
    
    if test_number(up, down) == True:
        print(game_start(up, down))
