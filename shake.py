from win32api import *
from win32con import *
from win32gui import *
import random

def main():
    while True:
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), w, h, hdc, 0, 0, SRCCOPY)
        BitBlt(hdc, 0, 0, w, h, hdc, random.randint(-10, 10), random.randint(-10, 10), SRCCOPY)
        ReleaseDC(0, hdc)

main()
