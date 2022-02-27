import time
import keyboard
import pyautogui
from win32api import GetSystemMetrics


def check_exit():
    if keyboard.is_pressed('f9'):
        return False
    else:
        return True


def main():
    print('Нажмите Ctrl-C для выхода.')
    print("width =", GetSystemMetrics(0))
    print("height =", GetSystemMetrics(1))
    switch = 1
    try:
        while check_exit():
            if keyboard.is_pressed('f10'):
                switch = abs(abs(0 - switch) - 1)
                time.sleep(0.5)
            while switch == 1 and check_exit():
                if keyboard.is_pressed('f10'):
                    switch = abs(abs(0 - switch) - 1)
                    time.sleep(0.5)
                check_exit()
                # Получение и вывод координат курсора, а также RGB-цвета пикселя под ним
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                pixelColor = pyautogui.screenshot().getpixel((x, y))
                positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
                positionStr += ', ' + str(pixelColor[1]).rjust(3)
                positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
                print(positionStr, end='')
                print('\b' * len(positionStr), end='', flush=True)

    except KeyboardInterrupt:
        print('\nГотово.')


if __name__ == '__main__':
    main()

