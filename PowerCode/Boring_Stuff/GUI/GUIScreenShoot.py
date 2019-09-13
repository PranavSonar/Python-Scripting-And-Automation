import pyautogui
# pyautogui.hotkey('win','r')
# pyautogui.screenshot(current_screen)/


basedir="c:/Users/Vivek Kumar/Desktop/"
find_screen=basedir+"Find_Screen.png"

print(find_screen)
location=pyautogui.locateOnScreen(find_screen)
print(location)
pyautogui.click(993,400)
pyautogui.typewrite("Hello word",interval=.2)



# pyautogui.alert(text='', title='', button='OK')
# pyautogui.confirm(text='fgf', title='fHello wordHello wordg', buttons=['OK', 'Cancel'])
# pyautogui.prompt(text='', title='' , default='')

import pyautogui
# pyautogui.hotkey('win','r')
# pyautogui.screenshot(current_screen)/


basedir="c:/Users/Vivek Kumar/Desktop/"
find_screen=basedir+"Find_Screen.png"
# pyautogui.hotkey('win','d')

hi

while True:
    print(find_screen)
    location=pyautogui.locateOnScreen(find_screen)
    print(location)
    if location:
        pyautogui.click(720,7200)
        pyautogui.press('enter')
        pyautogui.typewrite("hi")
        pyautogui.press('enter')

