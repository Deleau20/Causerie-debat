# from pathlib import Path

# # p = Path("/Users/imac_16/Documents/index.html")
# n = Path.home().iterdir()
# for i in n:
#     if i.is_dir():
#         print(i)

# print(n)

# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.parent.parent)
# print(p.suffixes)
# print(p.parts)
# print(p.exists())
# print(p.is_dir())
# print(p.is_file())
# print(p.iterdir())

 
# créer / supprimer des fichiers
from pathlib import Path

p = Path("/Users/imac_16/Documents")
print(p)
p = p / "reade.txt"
p.touch()
print(p)

p.write_text("Bonjour je commence à l'instant")
p.read_text()

