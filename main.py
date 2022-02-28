# -*-coding:UTF-8 -*-
import time
import keyboard
import pyautogui
import cv2
import numpy as np
from matplotlib import pyplot as plt
from win32api import GetSystemMetrics


def check_exit():
    if keyboard.is_pressed('f9'):
        return False
    else:
        return True


methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']


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
                        r = rgb_search[0] + allowance_r
                        g = rgb_search[1] + allowance_r
                        b = rgb_search[2] + allowance_r
                        if rgb_screen[0] == r and rgb_screen[1] == g and rgb_screen[2] == b:
                            return True
    return False

def balancerSearch():
    # =====================
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
               'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

    for meth in methods:
        for small in range(1, 15):
            imageObj = pyautogui.screenshot(region=(800, 400, 1200, 900))
            large_image = cv2.cvtColor(np.array(imageObj), cv2.COLOR_BGR2GRAY)

            path = './af2/' + str(small) + '.png'
            small_image = cv2.imread(path, 0)

            method = cv2.TM_SQDIFF

            result = cv2.matchTemplate(small_image, large_image, method)

            # We want the minimum squared difference
            mn, _, mnLoc, _ = cv2.minMaxLoc(result)

            # Draw the rectangle:
            # Extract the coordinates of our best match
            MPx, MPy = mnLoc

            # Step 2: Get the size of the template. This is the same size as the match.
            trows, tcols = small_image.shape[:2]

            # Step 3: Draw the rectangle on large_image
            cv2.rectangle(large_image, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)
            return True
            # Display the original image with the rectangle around the match.
            cv2.imshow('output', large_image)

            # The image is only displayed if we call this
            cv2.waitKey(0)
    # =====================

def main():
    print('Нажмите Ctrl-C для выхода.')
    print("width =", GetSystemMetrics(0))
    print("height =", GetSystemMetrics(1))
    switch = 1

    rect = (1120, 600, 1300, 800)
    rgb_serach = (134, 129, 114)

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
                positionStr = ''
                # if not pixel_search(rect, rgb_serach, 6):
                #     keyboard.send('space')
                #     print('Клюет ')
                #     switch = 0
                #     break

                # доделять чтоб выводило да или нет
                # if not balancerSearch():
                #     print('Клюет ')
                #

                x, y = pyautogui.position()

                positionStr += 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
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
