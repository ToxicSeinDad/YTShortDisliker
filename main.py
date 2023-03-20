import os
import time
from pyautogui import *
import win32api, win32con
import winsound

def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#1360,550 für likes

print("How many Videos should get disliked?")
rnum = input(">")
num = int(rnum)
dliks = 0
print("Delay?")
d = input(">")
delay = int(d)
print("Bluescreen#3678 on top")
print("5 Seconds to go to youtube shorts | To quit press CRTL + C in the console!")
time.sleep(5)
for i in range (num):
    os.system(f"title Disliked Videos: {dliks} von {num}")
    time.sleep(delay)
    click(1360,645)
    press("down")
    dliks+=1
    print(f"[{dliks}] Disliked Video")
    winsound.Beep(250,250)

winsound.Beep(750,750)
print(f"Program finished ({dliks} / {num})")


