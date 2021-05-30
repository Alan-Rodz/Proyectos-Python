# Regresa el arreglo ordenado usando quicksort
def quicksort(arreglo):

    # Caso base: Arreglos con 0 o 1 elemento ya estan ordenados
    if len(arreglo) < 2:
        return arreglo

    # Caso recursivo
    else:
        pivote = arreglo[0]

        # Sub-arreglo con los elementos menores que el pivote
        menor = [i for i in arreglo[1:] if i <= pivote]

        # Sub-arreglo con los elementos mayores que el pivote
        mayor = [i for i in arreglo[1:] if i > pivote]

        # Regresamos la combinacion de menor + pivote + mayor
        return quicksort(menor) + [pivote] + quicksort(mayor)


print(quicksort([10, 5, 2, 3]))
