print("------------------------------")
print("---BUSCA UN NUMERO CONJUNTO---")
print("------------------------------")

# Definicio de la funcion

def BuscarDatoEnLista(datoABuscar, lista):

    r = False
    for i in lista:
        if i == datoABuscar:
            r = True

    return r

# Entrada
Dato = int(input("Numero a buscar: ")) # Se recibe el dato del usuario

# Procesamiento

lista = [1,2,3,4,5] # Se almacena una lista de datos

if BuscarDatoEnLista(Dato, lista):
    print("Lo encontre")
else:
    print("No lo encontre")

# Salida
print("Eso no era ")