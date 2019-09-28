import time
import os
import pyautogui
from pathlib import Path
path = str(Path(__file__).parent.absolute())
# print("Current Path :"+str(path))
os.chdir(str(path+'\Sample'))
# print(os.getcwd())
find_screen = 'Like.png'
# for i in range(10):
while True:
    location = pyautogui.locateOnScreen(find_screen)
    print(location)
    # pyautogui.displayMousePosition()
    if location:
        print("find at position : " + str(location))
        # print(dir(location))
        pyautogui.click(location)
        # pyautogui.click(location.left, location.top+10)
        # pyautogui.press('enter')
        # pyautogui.typewrite("filefs")
        # pyautogui.press('enter')
else:
    print("Find Image Not Found.")

# time.sleep(0.001)
