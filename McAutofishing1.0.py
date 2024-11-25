import pyautogui
import time
import threading
print("Skrypt na wędkę by klepek, Ultimate build 1.0")
print("GUI scale 3, Show subtitles")
def gigawedkaeng():
    try:
        return pyautogui.locateOnScreen('gigawedka.png', confidence=0.8, grayscale=True) is not None
    except pyautogui.ImageNotFoundException:
        return False
    
def megagigasusattackfromnigger():
    try:
        return pyautogui.locateOnScreen('playerhurts.png', confidence=0.85, grayscale=True) is not None
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
    while gigawedkaeng() is False:
        time.sleep(0.1)
    print("złapano")
    pyautogui.rightClick()

def megagigasusattackfromniggerdetector():
    while megagigasusattackfromnigger() is False:
        time.sleep(0.1)
    print("Critical demage, ESC")
    pyautogui.keyDown('esc')

if __name__ == "__main__":
    mainstart = threading.Thread(target=main)
    susstart = threading.Thread(target=megagigasusattackfromniggerdetector)
    mainstart.start()
    susstart.start()
