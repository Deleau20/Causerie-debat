from typing import Any, Literal


class Carte:

    def __init__(self,nom: str, tipes: Literal["epique", "legendaire", "rare"], PV: float, PA: float):
        self.nom = nom
        self.tipes = tipes
        self.PV = PV
        self.PA = PA
    
    def sePresenter(self):
        raise NotImplementedError("La methode se presenter doit être implémenté avant d'être utilisé")
    
    def attaquer(self, advers_card: "Carte"):
        