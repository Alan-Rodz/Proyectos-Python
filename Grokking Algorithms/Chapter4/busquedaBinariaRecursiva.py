# Regresa el indice de x en arreglo si esta presente, de otra forma -1
def busquedaBinariaRecursiva(arreglo, menor, mayor, elementoBuscado):

    # Caso Base
    if mayor >= menor:
        mid = (mayor + menor) // 2

        # El elemento esta en el medio
        if arreglo[mid] == elementoBuscado:
            return mid

        # Si es menor buscamos en el sub-arreglo izquierdo
        elif arreglo[mid] > elementoBuscado:
            return busquedaBinariaRecursiva(arreglo, menor, mid - 1, elementoBuscado)

        # De otra manera buscamos en el sub-arreglo derecho
        else:
            return busquedaBinariaRecursiva(arreglo, mid + 1, mayor, elementoBuscado)

    # El elemento no esta en el arreglo
    else:
        return -1


# Arreglo de prueba
arr = [2, 3, 4, 10, 40]
x = 10

resultado = busquedaBinariaRecursiva(arr, 0, len(arr)-1, x)

if resultado != -1:
    print("Elemento en el indice", str(resultado))
else:
    print("El elemento no esta en el arreglo")
