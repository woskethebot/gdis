from win32api import *
from win32con import *
from win32gui import *

def main():
    while True:
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, 0, 0, w, h, hdc, 0, -20, SRCCOPY)
        ReleaseDC(0, hdc)

main()