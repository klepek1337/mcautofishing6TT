import pyautogui
import time
import threading
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  

print("Minecraft Autofishing script made by klepek")
print("GUI scale 3, Show subtitles")

image_directory = os.path.join(os.path.expanduser("~"), "Images")
gigawedka_path = os.path.join(image_directory, "gigawedka.png")
playerhurts_path = os.path.join(image_directory, "playerhurts.png")
wedka_path = os.path.join(image_directory, "g.png")


fish_count = 0
attack_count = 0


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

# Fonction principale du script
def main():
    print("Rightclick")
    wejscie()
    gigawedkadetector()
    main()

def wejscie():
    print("entry")
    time.sleep(5)
    pyautogui.rightClick()

def gigawedkadetector():
    global fish_count
    while not gigawedkaeng():
        time.sleep(0.1)
    print("catch")
    pyautogui.rightClick()
    fish_count += 1
    update_fish_count()

def megagigasusattackfromniggerdetector():
    global attack_count
    while not megagigasusattackfromnigger():
        time.sleep(0.1)
    print("Critical damage, ESC")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    attack_count += 1
    update_attack_count()

# GUI setup
def update_fish_count():
    fish_count_label.config(text=f"Fiches attrapées : {fish_count}")

def update_attack_count():
    alert_count.config(text=f"Tu as été attaqué : {attack_count}")

# Fonction pour démarrer le script
def start_script():
    main_thread = threading.Thread(target=main)
    sus_thread = threading.Thread(target=megagigasusattackfromniggerdetector)
    main_thread.start()
    sus_thread.start()

# Code principal
if __name__ == "__main__":
    if not os.path.exists(image_directory):
        print(f"Directory does not exist: {image_directory}")
    else:
        print(f"Using images from: {image_directory}")


    root = tk.Tk()
    root.title("McAutofishing1.0 by klepek")
    root.geometry("400x120")
    root.config(bg="black")  

   
    try:
        image = Image.open(os.path.join(image_directory, "g.png"))
        image = image.resize((50, 50))  
        image_tk = ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image: {e}")
        image_tk = None

   
    fish_count_label = ttk.Label(root, text="Fish catched : 0", font=("Helvetica", 14), background="white")
    fish_count_label.pack(pady=10)

    if image_tk:
        image_label = ttk.Label(root, image=image_tk, background="black")
        image_label.image = image_tk  
        image_label.place(x=10, y=10)

    
    alert_count = ttk.Label(root, text="You have been attacked: 0", font=("Helvetica", 10), background="red")
    alert_count.pack(pady=0)

   
    start_button = ttk.Button(root, text="Start", command=start_script)
    start_button.pack(pady=10)

    
    root.mainloop()
