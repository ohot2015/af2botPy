import pyautogui
from win32api import GetSystemMetrics
import keyboard
import time


def main():
    bot_is_active = True
    print('Нажмите Ctrl-C для выхода.')
    #    print(pyautogui.KEYBOARD_KEYS)
    print("width =", GetSystemMetrics(0))
    print("height =", GetSystemMetrics(1))

    try:
        # выходит при нажатии на f9
        while True:
            if keyboard.is_pressed('f9'):
                time.sleep(0.1)
                bot_is_active = True
        #pui
            while bot_is_active:
                if keyboard.is_pressed('f9'):
                    time.sleep(0.1)
                    bot_is_active = False
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
