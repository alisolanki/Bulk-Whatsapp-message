import webbrowser
import time
import pyautogui as gui

interval = 1
position = 935,409
position2 = 933,500
numbers = {999999999,8888888888,7777777777}

message="Your *Text*.%0A%0APlace it here."

for i in numbers:
    url = 'https://wa.me/91{}?text={}'.format(i, message)
    webbrowser.open(url)
    time.sleep(3)
    gui.click(position)
    time.sleep(2)
    gui.click(position2)
    time.sleep(7)
    gui.press('enter')
    time.sleep(interval)
