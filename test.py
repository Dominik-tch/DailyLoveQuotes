import tkinter as tk
from tkinter import filedialog
import shutil
import os

def select_file_and_copy():
    # Benutzer lässt eine JSON-Datei auswählen
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    
    if file_path:
        # Zielpfad im Repository
        repo_data_folder = "data"
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(repo_data_folder, file_name)
        
        # Kopiere die Datei
        shutil.copy(file_path, destination_path)
        print(f"Datei '{file_name}' wurde ins Repository kopiert.")

# Tkinter root Fenster erstellen und schließen
root = tk.Tk()
root.withdraw()  # Fenster nicht anzeigen
select_file_and_copy()