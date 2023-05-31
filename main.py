import pyautogui
from time import sleep
import easyPWD_Generate as pg
"""
print("be ready")
sleep(5)
print("rq")
sleep(2)
"""
nb=10
def rp(f):
    
    pyautogui.hotkey('win')
    sleep(0.1)
    if(f):
        pyautogui.typewrite("https://rewards.bing.com/")
        sleep(0.1)
        pyautogui.hotkey('enter')
    else:
        pyautogui.typewrite(pg.generatepwd(len=30))
        sleep(0.1)
        pyautogui.hotkey('enter')
        sleep(2)
        pyautogui.hotkey('Alt', 'F4')
        sleep(0.5)
for i in range(nb):
    rp(i==nb)
