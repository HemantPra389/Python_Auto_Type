import pyautogui
import time
import webbrowser as wb

wb.open("https://web.whatsapp.com/")


time.sleep(20)
for i in range(5000):
    pyautogui.typewrite('Write Your Own Text !')
    pyautogui.press("enter")
