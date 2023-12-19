from win32api import *
from win32gui import *
import time
import random

def main():
    while True:
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        color = RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        brush = CreateSolidBrush(color)
        x1, y1, x2, y2 = random.randint(0, w), random.randint(0, h), random.randint(0, w), random.randint(0, h)
        SelectObject(hdc, brush)
        Ellipse(hdc, x1, y1, x2, y2)
        DeleteObject(brush)
        time.sleep(0.01)
        ReleaseDC(0, hdc)

main()
