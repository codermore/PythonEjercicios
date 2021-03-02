"""
Gabriel Maso

Programa: 
Escribi una funcion que dada una cadena de caracteres, devuelva:
a) La primera letra de cada palabra. Por ejemplo, Si recibe 'Universal Serial Bus'
deve devolver 'USB'.
b) Dicha cadena con la primera letra de cada palabra en mayusculas. Por ejemplo, si recibe
'Republica argentina' deberia devolver 'Republica Argentina
c) Las palabras que comiencen con la letra 'A'. Por ejemplo, si recibe 'Antes de ayer' debe devolver 'antes ayer'
"""

def primeraLetra (oracion):
    palabras = oracion.split(' ')
    primeras_letras = ""
    for palabra in palabras:
        primeras_letras += palabra[0]
    return primeras_letras

def subirLevel (oracion):
    palabras = oracion.split(" ")
    primeras_mayusculas = ""
    for palabra in palabras:
        primeras_mayusculas += palabra.capitalize() + " "
    return primeras_mayusculas

def onlyA (oracion):
    palabras = oracion.split(" ")
    solo_a = ""
    for palabra in palabras:
        if palabra[0] == 'a' or palabra[0] == 'A':
            solo_a += palabra + " "
    return solo_a


oracion = input("ingrese oracion:")
print(primeraLetra(oracion))
print(subirLevel(oracion))
print(onlyA(oracion))

