import pyautogui, time, os

def spamer(v, n, t=3):
    time.sleep(t)
    for i in range(n):
            pyautogui.typewrite(v)
            pyautogui.press("enter")