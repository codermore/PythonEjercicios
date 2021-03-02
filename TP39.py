"""
Gabriel Maso

Programa: 
Modificar las funciones anteriores (TP34), para que recibasn un parametro que indique la cantidad máxima de reemplazos
o inserciones a realizar 
"""

def separar (palabra,caracter,num):    
    x = 0
    retorno = ""
    for letra in palabra:
        if x<num: 
            retorno += letra + caracter
            x+=1
        else:
            retorno += letra 
    return retorno

def reemplazar(palabra,caracter,num):
    vocales = " "
    reemplazo = ""
    x= 0
    for letra in palabra:
        if x<num:
            if letra not in vocales:
                reemplazo += letra
            else:
                reemplazo += caracter
                x+=1
        else:
            reemplazo += letra
    return reemplazo

def mascara (palabra,caracter,num):    
    x=0
    retorno = ""
    for letra in palabra:
        if x<num:
            retorno += caracter
        else:
            retorno += letra
        x+=1
    return retorno

def numero (palabra,caracter,num):
    x = 0
    y = 0
    result = 1
    retorno = ""
    while x < len(palabra):
        if x != 0: 
            result = x % 3
        if result == 0 and y<num:
            retorno += caracter + palabra[x]
            y +=1
        else:
            retorno += palabra[x]
        x+=1
    return retorno 
        
 

# bloque principal

palabra = input("ingerese una palabra: ")
caracter = input("ingrese un caracter: ")
num = int(input("ingrese maximo de inserciones: "))

print (separar(palabra,caracter,num))
print (reemplazar(palabra,caracter,num))
print ("su nueva clave es:",mascara(palabra,caracter,num))
print (numero(palabra,caracter,num))



