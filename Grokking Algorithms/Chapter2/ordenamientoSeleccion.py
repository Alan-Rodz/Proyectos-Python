# Recibe un arreglo y devuelve el indice del menor elemento que contenga
def encontrarMenor(arreglo):

    # Variable que guarda el elemento mas pequeño del arreglo
    menor = arreglo[0]

    # Variable que guarda el indice del valor menor
    indice_menor = 0

    for i in range(1, len(arreglo)):
        if arreglo[i] < menor:
            menor = arreglo[i]
            indice_menor = i

    return indice_menor


# Ordena un arreglo
def ordenamientoSeleccion(arreglo):
    nuevoArreglo = []
    for i in range(len(arreglo)):
        menor = encontrarMenor(arreglo)
        nuevoArreglo.append(arreglo.pop(menor))
    return nuevoArreglo


print(ordenamientoSeleccion([5, 3, 6, 2, 10]))
