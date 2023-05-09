from pathlib import Path
from typing import List, Dict, TypedDict
from pprint import pprint


class Dico(TypedDict):
    extensions: List[str]
    fichiers: List[Path]
    

downloads: Path = Path.home() / "Téléchargements"
dico: Dict[str,Dico] = {
    "Images":{
        "extensions":[".jpg",".png",".jpeg",".svg",".ico"],
        "fichiers":[]
    },
    "Python":{
        "extensions":[".py", ".pyc"],
        "fichiers":[]
    },
    "Documents":{
        "extensions":[".txt",".pdf",".doc",".html",".url",".db",".css"],
        "fichiers":[]
    },    
    "Videos":{
        "extensions":[".mp4",".avi"],
        "fichiers":[]
    },
    "Musiques":{
        "extensions":[".mp3",".m4a"],
        "fichiers":[]
    },
    "Archives":{
        "extensions":[".zip",".rar",".tar.xz"],
        "fichiers":[]
    },
    "Programmes":{
        "extensions":[".dmg",".pkg",".iso"],
        "fichiers":[]
    },
    "Autres":{
        "extensions":[],
        "fichiers":[]
    },
}

iterable = downloads.iterdir()
files: List[Path] =  [f for f in iterable if f.is_file()]
for folder, value in dico.items():
    for f in files:
        if f.suffix.lower() in value["extensions"]:
            value["fichiers"].append(f)

for folder, value in dico.items():
    # concaténation dossiers(sous forme de clé du dico) au dossiers Downloads
    DIR = (downloads / folder)
    # création des dossiers(sous forme de clé du dico)
    DIR.mkdir(exist_ok=True)
    for f in value["fichiers"]:
       new_file = DIR / f.name
       f.rename(new_file)