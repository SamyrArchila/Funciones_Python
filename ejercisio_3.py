# Construir una funcion  que reciba como parametro  una lista de datos numericos y retorne la suma de dichos datos
import random

def sumar_lista_datos(lista_numeros):

    suma = 0
    for numero in lista:
        suma += numero
    return suma

lista = []

n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1,9)
    lista.append(num)
print("---------------------------------------")

print("Lista: ", lista)
print("La suma es: ", sumar_lista_datos(lista))

print("---------------------------------------")
print("Eso era") 
print("---------------------------------------")  