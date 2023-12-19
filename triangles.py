from win32api import *
from win32con import *
from win32gui import *
import random

def main():
    while True:
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        colors = (RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        hPen, hBrush = CreatePen(PS_SOLID, 2, colors[0]), CreateSolidBrush(colors[1])
        SelectObject(hdc, hPen), SelectObject(hdc, hBrush)
        Polygon(hdc, [(random.randint(0, w), random.randint(0, h)) for _ in range(3)])
        SelectObject(hdc, None), SelectObject(hdc, None)
        DeleteObject(hPen), DeleteObject(hBrush)
        ReleaseDC(0, hdc)

main()