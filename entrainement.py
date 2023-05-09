# NOMBRE PREMIER
# def is_prime(n):
#   for i in range(2,n):
#     if (n%i) == 0:
#       return False
#   return True


# print(is_prime(19))


# INVERSE TABLEAU
# def inverse(tab, tailleTableau, i1, i2):
#     if i1 >tailleTableau or i2 > tailleTableau:
#         return -1
#     else:
#         tab[i1], tab[i2] = tab[i2], tab[i1]
#         return tab


# print(inverse([1,2,7,8,9],4,3,0))


def mul(n):
    if type(n) is int:
        tab = []
        for i in range(1,11):
            tab.append(str(n*i))
        res = ",".join(tab[0:6])+",...,"+str(tab[-1])

        return res
    else:
        return -1
print(mul(2))