from pathlib import Path
import shutil

# Chemin du dossier Téléchargements
downloads_path = Path.home() / "Downloads"

# Créer un dictionnaire pour stocker les extensions et les dossiers correspondants
extensions_folders = {
    "png": "Images",
    "jpg": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "pdf": "PDF",
    "doc": "Documents",
    "docx": "Documents",
    "xls": "Documents",
    "xlsx": "Documents",
    "ppt": "Présentations",
    "pptx": "Présentations",
    "zip": "Archives",
    "rar": "Archives",
    "exe": "Programmes",
    "dmg": "Programmes",
    "txt": "Textes",
    "csv": "Textes",
    "mp4": "Videos",
    "mkv":  "Videos",
    "html": "Sites Web",
    "fig": "Figma",
    "mp3": "Musique",
    
}

# Parcourir tous les fichiers dans le dossier Téléchargements
for file_path in downloads_path.iterdir():
    if file_path.is_file():
        # Obtenir l'extension du fichier
        extension = file_path.suffix[1:]
        # Si l'extension est répertoriée dans le dictionnaire, déplacer le fichier vers le dossier correspondant
        if extension in extensions_folders:
            folder_name = extensions_folders[extension]
            folder_path = downloads_path / folder_name
            folder = extensions_folders.get(extension, "Autres")
            folder_path.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(folder_path / file_path.name))
