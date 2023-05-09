# import requests

# nom = requests.get('https://api.github.com/events', auth=('user', 'pass'))
# print(nom)

nbr = input("Entrez un nombre à multiflier : ")
def code(nbr):
    
    if type(nbr) is int:
        tab = []
        for i in range(1,11):
            tab.append(str(nbr*i))
        res = ",".join(tab[0:6])+",...,"+str(tab[-1])
        print(res)
