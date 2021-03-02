"""
Gabriel Maso

Programa: 
Escribi una funcion que reciba una cadena que contiene un largo numero entero y
devuelva una cadena con el numero y las separaciones de miles.
Por ejemplo: 1234567890 -> devuelve: 1.234.567.890
"""

def formato (palabra):
    return ('{:,}'.format(palabra).replace(',','.'))

palabra = int(input("ingerese una numero: "))

print (formato(palabra))


