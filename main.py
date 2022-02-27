import time
import keyboard
import pyautogui
from win32api import GetSystemMetrics


def check_exit():
    if keyboard.is_pressed('f9'):
        return False
    else:
        return True


def pixel_search(rect, rgb_search, allowance=1):
    screenshot = pyautogui.screenshot()
    if allowance == 0:
        allowance = 1
    for i in range(rect[0], rect[2]):
        for j in range(rect[1], rect[3]):
            rgb_screen = screenshot.getpixel((i, j))
            for allowance_r in range(0, allowance):
                for allowance_g in range(0, allowance):
                    for allowance_b in range(0, allowance):
                        print(i, j, rgb_screen)
                        r = rgb_search[0] + allowance_r
                        g = rgb_search[1] + allowance_g
                        b = rgb_search[2] + allowance_b
                        if rgb_screen[0] == r and rgb_screen[1] == g and rgb_screen[2] == b:
                            print(i, j)
                            return True
    return False


def main():
    print('Нажмите Ctrl-C для выхода.')
    print("width =", GetSystemMetrics(0))
    print("height =", GetSystemMetrics(1))
    switch = 1

    rect = (0, 0, 130, 90)
    rgb_serach = (255, 0, 0)

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
                if pixel_search(rect, rgb_serach, 10):
                    print('gooooooood')
                return False
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
