import pyautogui
import os
import time
from pathlib import Path
path = str(Path(__file__).parent.absolute())
# print("Current Path :"+str(path))
os.chdir(str(path+'\Sample'))
major_check_sample='Major Check.png'
allow_sample = 'bit9_allow_sample.png'
allow_find_location=None
# pyautogui.hotkey('win','d')
# for i in range(10):
while True:
    major_find_location=pyautogui.locateOnScreen(major_check_sample)
    if major_find_location:
        print("Major Find :{}".format(major_find_location))
        allow_find_location = pyautogui.locateOnScreen(allow_sample)        
        # pyautogui.displayMousePosition()
        if allow_find_location:
            print("Allow Find : {}".format(allow_find_location))
            # get current position
            current_mouse_location=pyautogui.position()
            print("find at position : " + str(allow_find_location))
            # print(dir(location))
            pyautogui.click(allow_find_location)
            # Reset mouse position to its previous place
            pyautogui.moveTo(current_mouse_location)        
            # pyautogui.hotkey('win','r')
            # pyautogui.click(location.left, location.top+10)
            # pyautogui.press('enter')
            # pyautogui.typewrite("filefs")
            # pyautogui.press('enter')
        else:
            print("Allow Sample image Not Found.")
    else:
        print("No Bit9 Warning")
        if allow_find_location:
            current_mouse_location=pyautogui.position()
            # print(dir(location))
            pyautogui.click(allow_find_location)
            print("Still Clicking")
            # Reset mouse position to its previous place
            pyautogui.moveTo(current_mouse_location) 