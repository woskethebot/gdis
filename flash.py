# thanks to malwux on discord for giving me this code (had alot of syntax errors but i fixed and modified it)

from win32api import *
from win32con import *
from win32gui import *
import time

def main():
    while True:
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        PatBlt(hdc, 0, 0, w, h, PATINVERT)
        time.sleep(1)
        ReleaseDC(0, hdc)

main()