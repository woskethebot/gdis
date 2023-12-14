import random
import ctypes
import time
import win32gui
import win32api

screen_width = win32api.GetSystemMetrics(0)
lptext = "your text here"

def main():
    while True:
        hdc = win32gui.GetDC(0)
        text_color = random.randint(0, 255) | (random.randint(0, 255) << 8) | (random.randint(0, 255) << 16)
        ctypes.windll.gdi32.SetTextColor(hdc, text_color)
        ctypes.windll.gdi32.SetBkMode(hdc, 0)
        x, y = random.randint(0, screen_width), random.randint(0, screen_width)
        ctypes.windll.gdi32.TextOutW(hdc, x, y, lptext, len(lptext))
        ctypes.windll.user32.ReleaseDC(ctypes.windll.user32.GetDesktopWindow(), hdc)

main()