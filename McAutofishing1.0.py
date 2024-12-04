import pyautogui
import time
import threading
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageEnhance

print("Minecraft Autofishing script made by klepek")
print("GUI scale 3, Show subtitles")

image_directory = os.path.join(os.path.expanduser("~"), "Images")
gigawedka_path = os.path.join(image_directory, "gigawedka.png")
playerhurts_path = os.path.join(image_directory, "playerhurts.png")
wedka_path = os.path.join(image_directory, "g.png")
jeden_path = os.path.join(image_directory, "1.png")

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


def fade_out(image_label, image_path, duration=2000, steps=20):
    """
    Animuje zanikanie obrazu, zmniejszając jego jasność.
    :param image_label: Etykieta wyświetlająca obraz.
    :param image_path: Ścieżka do obrazu.
    :param duration: Całkowity czas zanikania w milisekundach.
    :param steps: Liczba kroków animacji.
    """
    try:
        original_image = Image.open(image_path)
        step_time = duration // steps
        enhancer = ImageEnhance.Brightness(original_image)

        def step(fade_step=0):
            if fade_step <= steps:
                brightness = 1 - (fade_step / steps)  # Obliczamy jasność (od 1 do 0)
                faded_image = enhancer.enhance(brightness)
                faded_image_tk = ImageTk.PhotoImage(faded_image)
                image_label.config(image=faded_image_tk)
                image_label.image = faded_image_tk  # Zachowujemy referencję
                root.after(step_time, step, fade_step + 1)  # Następny krok
            else:
                image_label.config(image="")  # Usuwamy obraz po zakończeniu animacji
                image_label.image = None

        step()  # Rozpoczynamy animację
    except Exception as e:
        print(f"Error during fade_out: {e}")


def update_fish_count():
    global fish_image_label
    fish_count_label.config(text=f"Fish Catched : {fish_count}")
    try:
        image = Image.open(jeden_path)
        image = image.resize((50, 50))
        image_tk = ImageTk.PhotoImage(image)
        fish_image_label.config(image=image_tk)
        fish_image_label.image = image_tk
        fish_image_label.place(x=340, y=10)  # Wyświetl obraz w prawym górnym rogu
        fade_out(fish_image_label, jeden_path, duration=2000, steps=20)  # Zanikanie obrazu
    except Exception as e:
        print(f"Error loading image: {e}")


def update_attack_count():
    alert_count.config(text=f"You have been attacked : {attack_count}")


def start_script():
    main_thread = threading.Thread(target=main)
    sus_thread = threading.Thread(target=megagigasusattackfromniggerdetector)
    main_thread.start()
    sus_thread.start()


def start_script_with_feedback():
    start_button.config(text="Started")  # Zmiana tekstu przycisku na 'Started'
    start_script()  # Rozpoczęcie głównego skryptu


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

    # Dodanie przycisku z funkcją animacji
    start_button = ttk.Button(root, text="Start", command=start_script_with_feedback)

    
    alert_count = ttk.Label(root, text="You have been attacked: 0", font=("Helvetica", 10), background="red")
    alert_count.pack(pady=0)

   
    start_button = ttk.Button(root, text="Start", command=start_script)

    start_button.pack(pady=10)

    fish_image_label = ttk.Label(root, background="black")
    fish_image_label.pack(pady=5)

    root.mainloop()
