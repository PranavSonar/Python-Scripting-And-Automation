import pyautogui
# pyautogui.hotkey('win','r')
import time
find_screen = "c:/Users/Vivek Kumar/Desktop/Find_Screen.png"
# pyautogui.hotkey('win','d')
while True:
    location = pyautogui.locateOnScreen(find_screen)
    print(location)
    # pyautogui.displayMousePosition()
    if location:
        print("find at position : "+str(location))
        pyautogui.click(875, 930)
        pyautogui.press('enter')
        # pyautogui.typewrite("filefs")
        pyautogui.press('enter')
    else: 
        print("Find Image Not Found.")
    time.sleep(10)
