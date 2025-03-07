# Construir una funcion  que reciba como parametro  una lista de datos numericos y retorne la suma de dichos datos

def sumar_lista(lista_numeros):

    suma = 0
    for numero in lista_numeros:
        suma += numero
    return suma


lista = [1, 2, 3, 4, 5]
print(sumar_lista(lista))  