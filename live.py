# def sopp(t):
#     return list(set(t))

# print(sopp([1,2,1,5,6,6,1,2,3,1,2,3,1,2,3,4]))


# def moyenne(tableau):
#     for nombre in tableau:
#         if type(nombre) != int or nombre < 0:
#             return -1
#     total = sum(tableau)
#     moyenne = total / len(tableau)
#     if moyenne % 1 != 0:
#         moyenne = round(moyenne)
#     return int(moyenne)

# print(moyenne([13,16,15]))

# def divide(x, y):
#     if type(x) != int or type(y) != int:
#         return -1
#     if y == 0 or x < 0 or y < 0:
#         return -1
#     quotient = x / y
    
#     return quotient 

# print(divide(1,2))

def hasDistinct_element(t):
    if not isinstance(arr, list) or not all(isinstance(num, (int, float)) for num in arr):
                return -1
            
            # Vérifier si tous les éléments du tableau sont distincts
            if len(set(arr)) == len(arr):
                return True
            else:
                return False

print(hasDistinctElements([1,2,3,4,5,5]))

def matrixSort(matrix):

    """ Fonction qui permet le trie des éléments d'une matrix carrée

    Args:
        matrix : matrix carrée d'entier

    return:
        list : retourne une matrix carrée avec ces éléments trié dans l'ordre croissant
    """

    # on fait un trie de chaque élements de la matrix contenu dqns chaque ligne
    trie = [item for row in matrix for item in row]
    trie.sort()
    taille = len(matrix)

    matrix_trier = [trie[i*taille : (i+1)*taille] for i in range(taille)]

    return matrix_trier


print(matrixSort([[3,5,7],[1,9,4],[8,2,6]]))