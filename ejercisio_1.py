# Construir una funcion que reciba su nombre como parametro y que lo muestre 5 veces en la pantalla

def mostrar_nombre(nombre):

    for i in range(1, 6): 
        print(f"{i}. {nombre}")

print("------------------")
mostrar_nombre("Samyr")
print("------------------")