# Construir una funcion que reciba como parametro una lista de datos numericos y que retorne el promedio de dichos datos 
import random

def calcular_promedio_lista(lista):

    suma = 0
    for i in lista:
        suma = suma + i
    promedio = suma / len(lista)
    return promedio

lista = []

n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(14,18)
    lista.append(num)

    print("Lista: ", lista)
print("El promedio de la lista es: ", calcular_promedio_lista(lista))   

print("Eso era")