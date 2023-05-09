# Ecrire une fonction qui permet de vérifier si une chaine de caractère est un palindrome

def palindrome(v):
    reverse = v[::-1]
    if v==reverse:
        return True
    return False

mot = input("Entrer un mot : ")
if palindrome(mot):
    print(f"{mot} un un palindrome")

else:
    print(f"{mot} n'est pas un palindrome")

