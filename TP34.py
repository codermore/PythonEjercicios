"""
Gabriel Maso

Programa: 
Escribi funciones que dada una cadena y un caracter:
a) Inserte el caracter entre cada letra de la cadena. Ej: 'Separar' y ',' deberia 
devolver 'S,e,p,a,p,r,a,r'
b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
deberia devolver mi_archivo_.txt'
c) Reemplace los digitos en la cadena de caracter. Ej: 'su clave es: 1540' y 'X' deberia devolver 'su calve es: XXXX'
d) Inserte el caracter cada 3 digitos en la cadena. Ej. '2552552550' y '.' deberia devolver '255.255.255.0'
"""

def separar (palabra,caracter):    
    retorno = ""
    for letra in palabra:
        retorno += letra + caracter
    return retorno

def reemplazar (palabra,caracter):
    palabra = palabra.replace(" ", caracter)
    return palabra

def mascara (palabra,caracter):   
    retorno = ""
    for letra in palabra:
        retorno += caracter
    return retorno

def numero (palabra,caracter):
    x = 0
    result = 1
    retorno = ""
    while x < len(palabra):
        if x != 0: 
            result = x % 3
        if result == 0:
            retorno += caracter + palabra[x]
        else:
            retorno += palabra[x]
        x+=1
    return retorno 
        
 

# bloque principal

palabra = input("ingerese una palabra: ")
caracter = input("ingrese un caracter: ")

print(separar(palabra,caracter))
print(reemplazar(palabra,caracter))
print("su nueva clave es:", mascara(palabra,caracter))
print(numero(palabra,caracter))




