import win32gui
import win32api
import win32con
import random
import time

screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
hwnd = win32gui.GetDesktopWindow()
hdc = win32gui.GetWindowDC(hwnd)

def ellipse():
    for _ in range(5000):
        color = win32api.RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        brush = win32gui.CreateSolidBrush(color)
        x1, y1, x2, y2 = random.randint(0, screen_width), random.randint(0, screen_height), random.randint(0, screen_width), random.randint(0, screen_height)
        win32gui.SelectObject(hdc, brush)
        win32gui.Ellipse(hdc, x1, y1, x2, y2)
        win32gui.DeleteObject(brush)
        time.sleep(0.01)
    win32gui.ReleaseDC(hwnd, hdc)

ellipse()
