from typing import Any
from card import carte

class Epique(carte):

    def __init__(self, nom: str):
        super().__init__(nom, "epique")