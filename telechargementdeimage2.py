import requests
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

def download_image(img_url):
    # Définir un en-tête User-Agent pour simuler un navigateur
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    # Faire la requête HTTP pour récupérer l'image avec les en-têtes
    response = requests.get(img_url, headers=headers)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Ouvrir une boîte de dialogue pour choisir l'emplacement de sauvegarde
        Tk().withdraw()  # Masque la fenêtre principale Tkinter
        save_path = asksaveasfilename(
            title="Enregistrer l'image sous",
            defaultextension=".jpg",
            filetypes=[("Fichiers JPG", "*.jpg"), ("Tous les fichiers", "*.*")]
        )
        
        if save_path:  # Si un chemin a été sélectionné
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image téléchargée avec succès : {save_path}")
        else:
            print("Téléchargement annulé par l'utilisateur.")
    else:
        print(f"Échec du téléchargement de l'image. Code de statut: {response.status_code}")

# URL de l'image Imgur (exemple)
img_url = "https://i.imgur.com/8nLFCVP.png"  # Remplacez par l'URL de l'image que vous voulez télécharger
download_image(img_url)
