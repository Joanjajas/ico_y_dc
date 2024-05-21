import pyautogui
import time
import sys
from pynput import keyboard
from PIL import ImageChops, Image

running = True


def on_press(key):
    global running

    if key.char == "q":
        running = False


def bucle(contraseñitaa: str, last_screenshot):
    # file menu
    pyautogui.moveTo(90, 74)
    pyautogui.click()

    # load file
    pyautogui.moveTo(90, 94)
    pyautogui.click()

    # choose file
    time.sleep(0.3)
    pyautogui.moveTo(544, 279)
    pyautogui.click()

    # click open file
    pyautogui.moveTo(1120, 575)
    pyautogui.click()

    # input password
    pyautogui.moveTo(838, 471)
    pyautogui.click()
    pyautogui.typewrite(contraseñitaa, interval=0.01)

    # click ok to send password
    pyautogui.moveTo(689, 521)
    pyautogui.click()

    # click ok when password is incorrect
    pyautogui.moveTo(854, 546)
    pyautogui.click()

    screenshot = pyautogui.screenshot(region=(900, 700, 950, 750))

    print(f"Trying password: {contraseñitaa}")

    if last_screenshot is not None:
        screenshot.save("screenshot.png")
        last_screenshot.save("last_screenshot.png")
        if len(set(ImageChops.difference(screenshot, last_screenshot).getdata())) > 200:
            print(f"Password found: {contraseñitaa}")
            sys.exit()

    return screenshot


def main():
    global running

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    last_screenshot = None

    for i in range(537, 10000):
        if not running:
            break

        if i < 10:
            contraseñitaa = str(i).zfill(4)
            last_screenshot = bucle(contraseñitaa, last_screenshot)

        elif i < 100:
            contraseñitaa = str(i).zfill(4)
            last_screenshot = bucle(contraseñitaa, last_screenshot)

        elif i < 1000:
            contraseñitaa = str(i).zfill(4)
            last_screenshot = bucle(contraseñitaa, last_screenshot)

        else:
            contraseñitaa = str(i).zfill(4)
            last_screenshot = bucle(contraseñitaa, last_screenshot)

    listener.stop()


if __name__ == "__main__":
    main()
