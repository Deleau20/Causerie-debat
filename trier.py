from pathlib import Path

dico = {
    'Images': {'fichier =[]','extentions = []'},
    'Videos': {'fichier =[]','extentions = []'},
    'Documents': {'fichier =[]','extentions = []'},
    'Autres': {'fichier =[]','extentions = []'}
}

p = Path.home() / "downloads"
print(p)

# for f in p.iterdir():
#         if f.is_dir():
#                 files = dico['Documents']['fichier']
#                 print(f)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
# print(files)



















                

# files = [f for f in p.iterdir() if p.is_file()]

# for f in files:
#         sortir = p / dico.get(f.suffix, "Autres")
#         sortir.mkdir(exist_ok=True)
#         f.rename (sortir / f.name)