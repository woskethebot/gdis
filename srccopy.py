from win32api import *
from win32con import *
from win32gui import *
import random

def main():
    while True:
        w = GetSystemMetrics(0)
        h = GetSystemMetrics(1)
        hdc = GetDC(0)
        BitBlt(hdc, 10, 10, w, h, hdc, 1, 1, SRCCOPY)
        ReleaseDC(0, hdc)

main()
