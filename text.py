from win32api import *
from win32gui import *
import time
import random

def main():
    while True:
        w, hdc = GetSystemMetrics(0), GetDC(0)
        text = "your text here"
        color = random.randint(0, 255) | (random.randint(0, 255) << 8) | (random.randint(0, 255) << 16)
        SetTextColor(hdc, color)
        SetBkMode(hdc, 0)
        x, y = random.randint(0, w), random.randint(0, w)
        ExtTextOut(hdc, x, y, 0, None, text, None)
        time.sleep(0.001)
        ReleaseDC(0, hdc)

main()