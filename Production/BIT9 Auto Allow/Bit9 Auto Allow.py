import pyautogui
import os
import time
from pathlib import Path
path = str(Path(__file__).parent.absolute())
# print("Current Path :"+str(path))
os.chdir(str(path+'\Sample'))
find_screen = 'bit9_allow_pic.PNG'
# pyautogui.hotkey('win','d')
# for i in range(10):
while True:
    location = pyautogui.locateOnScreen(find_screen)
    print(location)
    # pyautogui.displayMousePosition()
    if location:
        # get current position
        current_mouse_location=pyautogui.position()
        print("find at position : " + str(location))
        # print(dir(location))
        pyautogui.click(location)
        # Reset mouse position to its previous place
        pyautogui.moveTo(current_mouse_location)        
        # pyautogui.hotkey('win','r')
        # pyautogui.click(location.left, location.top+10)
        # pyautogui.press('enter')
        # pyautogui.typewrite("filefs")
        # pyautogui.press('enter')
    else:
        print("Find Image Not Found.")
