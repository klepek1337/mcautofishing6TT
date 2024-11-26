import pyautogui
import time
import threading
import os

print("Script Minecraft pour Piocher, fait par Adrian")
print("GUI scale 3, Show subtitles")

image_directory = os.path.join(os.path.expanduser("~"), "Images")
gigawedka_path = os.path.join(image_directory, "gigawedka.png")
playerhurts_path = os.path.join(image_directory, "playerhurts.png")

def gigawedkaeng():
    try:
        return pyautogui.locateOnScreen(gigawedka_path, confidence=0.8, grayscale=True) is not None
    except pyautogui.ImageNotFoundException:
        return False

def megagigasusattackfromnigger():
    try:
        return pyautogui.locateOnScreen(playerhurts_path, confidence=0.85, grayscale=True) is not None
    except pyautogui.ImageNotFoundException:
        return False

def main():
    print("Rightclick")
    wejscie()
    gigawedkadetector()
    main()

def wejscie():
    print("wejscie")
    time.sleep(5)
    pyautogui.rightClick()

def gigawedkadetector():
    while not gigawedkaeng():
        time.sleep(0.1)
    print("złapano")
    pyautogui.rightClick()

def megagigasusattackfromniggerdetector():
    while not megagigasusattackfromnigger():
        time.sleep(0.1)
    print("Critical damage, ESC")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')

if __name__ == "__main__":

    if not os.path.exists(image_directory):
        print(f"Directory does not exist: {image_directory}")
    else:
        print(f"Using images from: {image_directory}")

    mainstart = threading.Thread(target=main)
    susstart = threading.Thread(target=megagigasusattackfromniggerdetector)
    mainstart.start()
    susstart.start()
