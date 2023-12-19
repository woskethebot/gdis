from win32api import *
from win32con import *
from win32gui import *
import time
import random

def main():
    while True:
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(0, 2), random.randint(0, 2), w, h, hdc, random.randint(0, 2), random.randint(0, 2), SRCPAINT)
        time.sleep(0.01)
        ReleaseDC(0, hdc)

main()
