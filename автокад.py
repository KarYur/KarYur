import pyautogui
import time

time.sleep(3)
distance = 300
pyautogui.typewrite('pline')
pyautogui.press('enter')

while distance > 0:
    pyautogui.leftClick()
    pyautogui.dragRel(distance,0)
    pyautogui.leftClick()
    distance = distance - 20
    pyautogui.dragRel(0, distance)
    pyautogui.leftClick()
    pyautogui.dragRel(-distance, 0)
    pyautogui.leftClick()
    distance = distance - 20
    pyautogui.dragRel(0, distance)