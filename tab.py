from typing import Any

class Array:

    tab = []
    
    def __init__(self,*args):
        self.tab = list(args)
                   
    def at(self,indice : int) -> Any or None:
        try:
            return self.tab[indice]
        except IndexError:
            return None
        
    def concat(self,tabT : list[Any]) -> list[Any]:
        '''Fonction qui contaterne les éléments d'un tableau'''

        if type(tabT) == list:
            tableau = self.copie()
            for item in tabT: tableau.append(item)

            return  tableau
        raise TypeError("L'élément doit être un tableau")
    

    def copie(self) -> list[Any]:
        return [item for item in self.tab]

    
    def fill(self,rpl : Any,a : int, b : int = -1) -> list[Any]:
        '''Fonction qui retourne la taille d'un tableau'''

        if a < self.length() and b < self.length():
            if b < 0:
                b = self.length() + b
            tableau1 = self.copie()
            for i in range(a, b+1):
                tableau1[i] = rpl
            return tableau1
        raise IndexError("Erreur d'indice" )

    
    def length(self):
        cpt = 0
        for _ in self.tab:
          cpt += 1
        return cpt
    
    def push(self, *args) -> int:
        self.tab = self.tab + list(args)
        return self.length()

    def filtre(self,func) -> list[Any]:
        result = []
        for i in self.tab:
            if func(i):
                result.append(i)
        return result
    
    def my_map(self,func):
        result = []
        for i in self.tab:
            result.append(func(i))
        return result
    
    def include(self, b : Any):
        return b in self.tab
    

      
if __name__ == "__main__":
    test = Array(23,56,20,"2","cd")
    test2 = Array(2,4,5)

    print(test.at(2))
    print(test.concat([1,3,5,7,8]))
    print(test.fill("salut", 1))
    print(test.length())
    print(test.push(1,5, "salut"))
    print(test.filtre(lambda x: type(x) is int))
    print(test.my_map(lambda x: f'{x}-salut'))
    print(test.include(20))



    