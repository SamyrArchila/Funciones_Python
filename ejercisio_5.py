# Construir una funcion que reciba como parametro una lista de datos numericos y retorne el promedio de los datos pares 

import random

contador_pares = 0

def calcular_promedio_pares(lista):
    suma = 0
    global contador_pares
    for i in lista:
        if i % 2 == 0:
            contador_pares += 1
            suma = suma + 1
    promedio = suma / contador_pares
    print(f"hay {contador_pares} pares")
    return promedio

lista = []

n = int(input("Digite el tamaño de la lista: "))
 
for i in range(n):
    num = random.randint(1,n)
    lista.append(num)

print(f"lista: {lista}")
print(f"el promedio de la lista {calcular_promedio_pares(lista)}")

