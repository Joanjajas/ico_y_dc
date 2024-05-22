import pyautogui
import time
import os
import sys
from PIL import ImageChops

LOOP_START = 541


def restart_quantum(first_run: bool = False):

    if not first_run:
        pyautogui.hotkey("command", "q")
        time.sleep(3)

    os.system("open /Applications/QuantumStudent_MACOS.app")
    time.sleep(2)

    # enter to the app
    pyautogui.moveTo(829, 548)
    pyautogui.click()
    time.sleep(2)

    # select documents
    pyautogui.moveTo(435, 255)
    pyautogui.click()
    time.sleep(0.5)

    # choose file
    pyautogui.moveTo(544, 279)
    pyautogui.click()
    time.sleep(0.5)

    # click open file
    pyautogui.moveTo(1120, 575)
    pyautogui.click()
    time.sleep(0.5)

    # input password
    pyautogui.moveTo(838, 471)
    pyautogui.click()
    pyautogui.typewrite("0000", interval=0.01)
    time.sleep(0.5)

    # click ok to send password
    pyautogui.moveTo(689, 521)
    pyautogui.click()
    time.sleep(0.5)

    # click ok when password is incorrect
    pyautogui.moveTo(854, 546)
    pyautogui.click()
    time.sleep(0.5)


def loop(passwd: str, last_screenshot):
    # file menu
    pyautogui.moveTo(90, 74)
    pyautogui.click()

    # load file
    pyautogui.moveTo(90, 94)
    pyautogui.click()
    time.sleep(0.3)

    # choose file
    pyautogui.moveTo(544, 279)
    pyautogui.click()

    # click open file
    pyautogui.moveTo(1120, 575)
    pyautogui.click()

    # input password
    pyautogui.moveTo(838, 471)
    pyautogui.click()
    pyautogui.typewrite(passwd, interval=0.01)

    # click ok to send password
    pyautogui.moveTo(689, 521)
    pyautogui.click()
    time.sleep(0.2)

    # click ok when password is incorrect
    pyautogui.moveTo(854, 546)
    pyautogui.click()

    screenshot = pyautogui.screenshot(region=(900, 700, 950, 750))

    print(f"Trying password: {passwd}")

    if last_screenshot is not None:
        if (
            len(set(ImageChops.difference(screenshot, last_screenshot).getdata()))
            > 2000
        ):
            print(f"Password found: {passwd}")

            with open("passwords.txt", "a") as f:
                f.write(passwd + "\n")

            sys.exit()

    return screenshot


def main():
    last_screenshot = None
    start_time = time.time()
    restart_quantum(first_run=True)

    for i in range(LOOP_START, 10000):
        if i % 10 == 0:
            print(
                f"Tried {i - LOOP_START} passwords in {time.time() - start_time} seconds"
            )

            start_time = time.time()
            restart_quantum()

        if i < 10:
            passwd = str(i).zfill(4)
            last_screenshot = loop(passwd, last_screenshot)

        elif i < 100:
            passwd = str(i).zfill(4)
            last_screenshot = loop(passwd, last_screenshot)

        elif i < 1000:
            passwd = str(i).zfill(4)
            last_screenshot = loop(passwd, last_screenshot)

        else:
            passwd = str(i).zfill(4)
            last_screenshot = loop(passwd, last_screenshot)


if __name__ == "__main__":
    main()
