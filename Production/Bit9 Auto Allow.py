import pyautogui
# pyautogui.hotkey('win','r')
import time

find_screen = 'bit9_allow_pic.PNG'
# pyautogui.hotkey('win','d')
# for i in range(10):
while True:
location = pyautogui.locateOnScreen(find_screen)
print(location)
# pyautogui.displayMousePosition()
if location:
print("find at position : " + str(location))
# print(dir(location))
pyautogui.click(location.left, location.top)
# pyautogui.click(location.left, location.top+10)
# pyautogui.press('enter')
# pyautogui.typewrite("filefs")
# pyautogui.press('enter')
else:
print("Find Image Not Found.")
time.sleep(0.01)