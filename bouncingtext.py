from win32api import *
from win32gui import *
import time
import random

def main():
    x, y = 0, 0
    signX, signY = 1, 1
    incrementor = 5
    while True:
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        text = "your text here"
        color = random.randint(0, 255) | (random.randint(0, 255) << 8) | (random.randint(0, 255) << 16)
        SetTextColor(hdc, color)
        SetBkMode(hdc, 0)
        ExtTextOut(hdc, x, y, 0, None, text, None)
        x += incrementor * signX
        y += incrementor * signY
        if y >= h or y <= 0:
            signY *= -1
        if x >= w or x <= 0:
            signX *= -1
        time.sleep(0.01)
        ReleaseDC(0, hdc)

main()