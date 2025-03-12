# Construir una funcion que reciba cadena digitada(como parametro) por el usuario y que lo muestre n veces en la pantalla. El valor de n tambien es digitado por el usuario 

def mostrar_cadena(cadena, n):

    n = int(n) 
    for _ in range(1,n+1):
        print(cadena)

print("------------------------------------------------------------------------------------------")
cadena = input("Repite la cadena: ")
n = int(input("Digite el número de veces que va a mostrar la cadena: "))
print("------------------------------------------------------------------------------------------")
mostrar_cadena(cadena, n)
print("------------------------------------------------")
print("Eso era")
print("------------------------------------------------------------------------------------------")