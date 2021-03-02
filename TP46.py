import random

"""
Gabriel Maso

Programa: 
Escribir una funcion que indique si dos fichas de domino encajan o no. 
Las fichas son recibidas con tuplas, por ejemplo: (3,4) y (5,4)
"""
si = 0

def compatibilidad (fichas):
    for x in range (len(fichas)):
        if fichas[x][1] == fichas[x+1][0] or fichas[x][0] == fichas[x+1][1] or fichas[x][1] == fichas[x+1][1] or  fichas[x][0] == fichas[x+1][0]:
            return 1
        else: 
            return 0


def cargar():
    dados=[]
    for x in range(2):
        lado_1= random.randint(0,6)
        lado_2= random.randint(0,6)
        dados.append((lado_1,lado_2))
        print(dados[x], end="")
    return dados

forzar = input("forzar compatibilidad? Si/No: ")

forzar = forzar.lower()
if forzar == 'si':
    while si == 0:
        mano = cargar()
        print("")
        si = compatibilidad(mano)
else:
    mano = cargar()
    si = compatibilidad(mano)


if si == 1:
    print ("encajan")
else:
    print ("no encajan")


