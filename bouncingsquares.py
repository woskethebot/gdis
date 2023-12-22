from win32api import *
from win32con import *
from win32gui import *
import random

def main():
    signX = 1
    signY = 1
    x = 10
    y = 10
    while True:
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        incrementor = 10
        x += incrementor * signX
        y += incrementor * signY
        top_x = 0 + x
        top_y = 0 + y
        bottom_x = 100 + x
        bottom_y = 100 + y
        brush = CreateSolidBrush(RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        SelectObject(hdc, brush)
        Rectangle(hdc, top_x, top_y, bottom_x, bottom_y)
        if y >= GetSystemMetrics(SM_CYSCREEN):
            signY = -1
        if x >= GetSystemMetrics(SM_CXSCREEN):
            signX = -1
        if y == 0:
            signY = 1
        if x == 0:
            signX = 1
        DeleteObject(brush)
        ReleaseDC(0, hdc)

main()