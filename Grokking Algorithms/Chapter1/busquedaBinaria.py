# Recibe una lista y el elemento que buscamos en esa lista
# Devuelve la posicion de la lista en la que se encuentra el elemento buscado
def busqueda_binaria(lista, elementoBuscado):

    limiteInferior = 0
    limiteSuperior = (len(lista)-1)

    while limiteInferior <= limiteSuperior:

        elementoMedio = (limiteInferior + limiteSuperior)
        suposicion = lista[elementoMedio]

        if suposicion == elementoBuscado:
            return elementoMedio

        if suposicion > elementoBuscado:
            limiteSuperior = elementoMedio - 1

        else:
            limiteInferior = elementoMedio + 1

    return None

lista = [1, 3, 5, 7, 9]

print(busqueda_binaria(lista, 3)) 
print(busqueda_binaria(lista, -1)) 
