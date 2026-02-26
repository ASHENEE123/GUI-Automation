import pyautogui
import time
pyautogui.press("win",interval=0.2)
pyautogui.write("chrome",interval=0.6)
pyautogui.press("enter")
time.sleep(0.2)
pyautogui.write("git branch and merge info",interval=0.5)
pyautogui.press("enter")
time.sleep(0.4)
pyautogui.hotkey('ctrl','w')
time.sleep(3)