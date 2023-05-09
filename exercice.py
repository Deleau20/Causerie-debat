def mostLegth(chaine):
    b=chaine.split()
    mostLegth = b[0]
    for carac in b:
        if len(carac) > len(mostLegth):
            mostLegth=carac
    return mostLegth
print("\n") 
print("Le plus long mot de cette phrase est : \n>_")  
print(mostLegth("Bonjour je suis moi"))


print("\n")


def rangement(tab):
    for item in tab:
        if type(item) is dict or type(item) is list:
            return -1
    n = len(tab)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if tab[j] < tab[min]:
                min = j
        tab[i], tab[min] = tab[min], tab[i]
    return tab
print("Le rangement dans l'ordre est : \n>_")
print(rangement([8,7,6,5,4,3,2,0,0.9,-1, 2**9]))


print("\n")


def frequence(mot):
    dico = {}
    for char in mot:
        if char.isalpha():
            char = char.lower()
            if char in dico:
                dico[char] += 1
            else:
                dico[char] = 1
    total = sum(dico.values())
    for char, count in dico.items():
        pourcent = (count / total) * 100
        res = round(pourcent,2)
        dico[char] = (f"{res}%")
    
    return dico

print("La frequence des lettres constituant cette phrase est : \n>_")
print(frequence("salut je suis moi et toi"))


print("\n")


def anagramme(mot,mots):
    for item in (mot and mots):
        if type(item) == dict or type(item) == list:
            return -1
        for item in mot:
            if len(mot) == len(mots):
                if mot in mots:
                    return "c'est un anagramme"
                else:
                    return"Ce n'est pas un anagramme"



print(anagramme("jourbon", "bonjour"))


