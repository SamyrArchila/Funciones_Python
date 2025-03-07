# Construir una funcion que reciba cadena digitada(como parametro) por el usuario y que lo muestre n veces en la pantalla. El valor de n tambien es digitado por el usuario 

def repetir_cadena(cadena, n):

    n = int(n) 
    for _ in range(n):
        print(cadena)

print("------------------------------------------------------------------------------------------")
cadena_usuario = input("Repite la cadena: ")
repeticiones_usuario = int(input("Ingrese el número de veces que va a repetir la cadena: "))
print("------------------------------------------------------------------------------------------")
repetir_cadena(cadena_usuario, repeticiones_usuario)