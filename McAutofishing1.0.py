import pyautogui
import time
import threading
import os
import tkinter as tk
from tkinter import ttk

print("Script Minecraft pour Piocher, fait par Adrian")
print("GUI scale 3, Show subtitles")

image_directory = os.path.join(os.path.expanduser("~"), "Images")
gigawedka_path = os.path.join(image_directory, "gigawedka.png")
playerhurts_path = os.path.join(image_directory, "playerhurts.png")


fish_count = 0

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
    global fish_count
    while not gigawedkaeng():
        time.sleep(0.1)
    print("złapano")
    pyautogui.rightClick()
    fish_count += 1
    update_fish_count()

def megagigasusattackfromniggerdetector():
    while not megagigasusattackfromnigger():
        time.sleep(0.1)
    print("Critical damage, ESC")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')


def update_fish_count():
    fish_count_label.config(text=f"Fiches attrapées : {fish_count}")

def start_script():
    main_thread = threading.Thread(target=main)
    sus_thread = threading.Thread(target=megagigasusattackfromniggerdetector)
    main_thread.start()
    sus_thread.start()

if __name__ == "__main__":
    if not os.path.exists(image_directory):
        print(f"Directory does not exist: {image_directory}")
    else:
        print(f"Using images from: {image_directory}")


    root = tk.Tk()
    root.title("McAutofishing 1.0")
    root.geometry("300x150")
    

    fish_count_label = ttk.Label(root, text="Fiches attrapées : 0", font=("Helvetica", 14))
    fish_count_label.pack(pady=10)


    start_button = ttk.Button(root, text="Démarrer le script", command=start_script)
    start_button.pack(pady=10)


    root.mainloop()




