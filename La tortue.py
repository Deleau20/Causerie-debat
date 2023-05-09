import turtle

t = turtle.Turtle()

# for i in range(0,5):
#     t.forward(40)
#     t.left(90)
#     t.forward(40)
#     t.right(90)

# def escalier(taille,nb,angle):
#     for i in range(0,nb):
#         t.forward(taille)
#         t.left(angle)
#         t.forward(taille)
#         t.right(angle)
#     t.forward(taille)

# print(escalier(60, 2, 90))

def texte(taille):
    for i in range(1):
        t.forward(taille)
        t.backward(taille//2)
        t.right(90)
        t.forward(taille)
        t.left(90)
        t.forward(taille//2)
        t.backward(taille)

print(texte(100))




turtle.done()