from win32api import *
from win32con import *
from win32gui import *
import random

def main():
    while True:
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        hdcDest = CreateCompatibleDC(hdc)
        hBitmap = CreateCompatibleBitmap(hdc, w, h)
        SelectObject(hdcDest, hBitmap)
        hBrush = CreateSolidBrush(RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        SelectObject(hdcDest, hBrush)
        Rectangle(hdcDest, 0, 0, w, h)
        BitBlt(hdc, 0, 0, w, h, hdcDest, 0, 0, SRCINVERT)
        DeleteObject(hBitmap)
        DeleteObject(hBrush)
        DeleteDC(hdcDest)
        ReleaseDC(0, hdc)

main()
