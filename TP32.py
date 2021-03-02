"""
Gabriel Maso

Programa: 
Escribi funciones que dada una cadena de caracteres:
a) Imprima los dos primeros caracteres
b) Imprima los ultimos tres caracteres 
c) Imprima dicha cadena cada dos caractere. Ej.:'Recta' deberia imprimir 'rca'
d) Dicha cadena den sentido inverso. Ej.: 'Hola mundo!' debe imprimir '!odnum aloh'
e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'refeljo' imprime reflejoojelfer
"""

def cadena(dato,palabra):
    dato2 = dato.lower()
    if dato2 == 'a':
        for x in range (2):
            print (palabra[x], end="")
    
    elif dato2 == 'b':
        y = len(palabra)
        for x in range (y-3,y):
            print (palabra[x], end="")

    elif dato2 == 'c':
        for x in range(0,len(palabra),2):
            print (palabra[x], end="")

    elif dato2 == 'd':
        x = len(palabra)
        while x>0:
            print (palabra[x-1], end="") 
            x = x - 1 
    
    elif dato2 == 'e':
        x = len(palabra)
        print(palabra, end="")
        while x>0:
            print (palabra[x-1], end="") 
            x = x - 1 
    else:
        print("la opcion ingresada es incorrecta")

            
palabra = input("ingrese una palabra: ")
print("""a) Imprima los dos primeros caracteres
b) Imprima los ultimos tres caracteres 
c) Imprima dicha cadena cada dos caractere. Ej.:'Recta' deberia imprimir 'rca'
d) Dicha cadena den sentido inverso. Ej.: 'Hola mundo!' debe imprimir '!odnum aloh'
e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'refeljo' imprime reflejoojelfer""")
dato = input("ingrese opcion: ")

cadena(dato,palabra)
