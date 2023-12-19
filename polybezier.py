from win32api import *
from win32con import *
from win32gui import *
import random

def main():
    while True:
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        p = [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h))]
        color = RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        hPen = CreatePen(PS_SOLID, 5, color)
        SelectObject(hdc, hPen)
        PolyBezier(hdc, p)
        DeleteObject(hPen)
        ReleaseDC(0, hdc)

main()