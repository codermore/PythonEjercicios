import random

"""
Gabriel Maso

Programa: 
a) Proponer una representacion con tuplas para las cartas de poker (francesas).
b) Escribir una funcion poker que reciba cinco cartas de la bandeja francesa e informe (devuelva el valor logico
correspondiente) si esas cartas forman o no un poker (es decir que hay 4 cartas con el mismo numero)
"""

baraja = ('corazon', 'pikas', 'trebol', 'diamantes')
si = 0
forzar = ""

def cargar():
    cartas=[]
    for x in range(5):
        palo= baraja[random.randint(0,3)]
        numero= random.randint(0,14)
        cartas.append((palo,numero))
        print(cartas[x])
    return cartas

def poker (tanda):
    pok = 0
    pok2 = 0
    pos_1 = tanda[0][1]
    pos_2 = tanda[1][1]
    for x in range(5):
        if pos_1 == tanda[x][1]:
            pok +=1
        if pos_2 == tanda[x][1]:
            pok2 +=1
    if pok >= 4 or pok2 >= 4:
        return 1
    else:
        return 0

forzar = input("Forzar poket? Si/No: ")

forzar = forzar.lower()
if forzar == 'si':
    while si == 0:
        tanda = cargar()
        print("------------")
        si = poker(tanda)
else:
    tanda = cargar()
    si = poker(tanda)


if si == 1:
    print ("POKER!")
else:
    print ("no hay poker")

