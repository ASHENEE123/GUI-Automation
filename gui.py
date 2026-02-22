import pyautogui
import time
pyautogui.press("win",interval=0.5)
time.sleep(1)
pyautogui.write("google chrome",interval=0.5)
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("what is PyAutoGui",interval=0.5)
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey('ctrl','w')