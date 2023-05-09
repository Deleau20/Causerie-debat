# def carre(num):
#     return num**2  

# nombre =[1, 2, 3, 4]
# for item in map(carre, nombre):
#     list(map(carre,nombre))
#     print(item)



def fact(n: int) -> int:
    '''Fonction de factorielle sans recussion'''
    if not isinstance(n, (int)):
        return -1
    if n == 0:
        return 1
    fact = 1
    i = 1
    while i < n:
        fact = fact * (i+1)
        i += 1
    return fact

print(fact(5))


def fact1(n: int) -> int:
    '''Fonction de factorielle avec recussion'''
    if not isinstance(n, (int)):
        return -1
    if not n:
        return 1
    return n * fact1(n - 1)

print(fact1(0))

def sommePremierCarre(n:int) -> int:
    '''Fonction qui retourne la somme des prémier carrée d'un nombre...recussion'''
    if not isinstance(n, (int)):
        return -1
    if n == 1:
        return 1
    return n**2 + sommePremierCarre(n-1)

print(sommePremierCarre(6))

def long(cha:str) -> int:
    '''Fonction qui retourne la longueur d'une chaine de caractère...avec recussion'''
    if not isinstance(cha, (str)):
        return -1
    if cha == '':
        return 0
    if cha == ' ':
        return ""# type: ignore
    return 1+long(cha[1:])

print(long(" hfuhf"))

def sommeListe(num: list[int]) -> int:
    '''Fonction qui retourne la somme de tous les éléments d'une liste...avec recussion'''
    if not isinstance(num, list) or not all(isinstance(item, int) for item in num):
        return -1
    if num == []:
        return 0
    return num[0] + sommeListe(num[1:])

print(sommeListe([1,2,3,4,7,7]))

def suiteFibonacci(fn: int) ->int:
    '''Fonction qui retourne la suite de la fibonacci...avec recussion'''
    if not isinstance(fn, int):
        return -1
    if fn == 0:
        return 0
    if fn == 1:
        return 1
    if fn <= 2:
        return 1
    return suiteFibonacci(fn-1)+suiteFibonacci(fn-2)


print(suiteFibonacci(7))


def suite(s:int) -> int:
    '''Fonction qui retourne la suite de la somme...avec recussion'''
    if not isinstance(s, int):
        return -1
    if s == 0:
        return 0
    if s == 1:
        return 1
    if s <= 2:
        return 1
    return (3*suite(s-1))+suite(s-2)

print(suite(3))
