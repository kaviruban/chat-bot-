import pyautogui
import time
time.sleep(7)
k=open('bot.txt','r')
for word in k:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(0.5)
