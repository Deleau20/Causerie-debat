
import json

num1= int(input("Entrez nombre1 : "))
num2= int(input("Entrez nombre2 : "))
def sum(a,b):
    try:
        if (type(a) is int) and (type(b) is int):
            return a+b
    except TypeError:
        return -1


r = sum(num1,num2)


with open("calculatrice.tx", "r") as file:
    file.write(json.dumps(r))
