from win32api import *
from win32con import *
from win32gui import *
import random

def main():
    while True:
        hdc = GetDC(0)
        w = GetSystemMetrics(0)
        h = GetSystemMetrics(1)
        BitBlt(hdc, random.randint(0, 1), random.randint(0, 1), w, h, hdc, random.randint(0, 1), random.randint(0, 1), SRCPAINT)
        ReleaseDC(0, hdc)

main()
