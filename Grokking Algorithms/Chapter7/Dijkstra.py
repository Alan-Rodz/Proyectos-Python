
import sys


class Grafo():

    # Constructor
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def imprimirSolucion(self, distancias):
        print("Vertice: \tDistancia del nodo inicial:")
        for nodo in range(self.V):
            print(nodo, "\t\t", distancias[nodo])

    # Encuetra el vertice con el valor de distancia minimo que todavia no se encuentra en el arbol-recorrido mas corto
    def distanciaMinima(self, distancias, recorridoMasCorto):

        # Inicializamos la distancia minima para el siguiente nodo
        minimo = sys.maxsize

        # Buscamos el vertice mas cercano en el recorrido mas corto
        for v in range(self.V):
            if distancias[v] < minimo and recorridoMasCorto[v] == False:
                minimo = distancias[v]
                indice_minimo = v

        return indice_minimo

    # Dijkstra con representacion de matriz de adyacencia
    def dijkstra(self, nodoInicial):

        distancias = [sys.maxsize] * self.V
        distancias[nodoInicial] = 0
        recorridoMinimo = [False] * self.V

        for iteracion in range(self.V):

            # Obtenemos el vertice con la distancia minima del conjunto de vertices todavia no procesados
            # u siempre es el nodoInicial en la primera iteracion
            u = self.distanciaMinima(distancias, recorridoMinimo)

            # Ponemos el vertice con la distancia minima en el recorridoMinimo
            recorridoMinimo[u] = True

            # Actualizamos el valor de la distancia de los vertices adyacentes al vertice elegido
            # Solamente si la distancia actual es mayor a la nueva distancia y el vertice no esta en el recorrido minimo
            for v in range(self.V):
                if self.graph[u][v] > 0 and recorridoMinimo[v] == False and distancias[v] > distancias[u] + self.graph[u][v]:
                    distancias[v] = distancias[u] + self.graph[u][v]

        self.imprimirSolucion(distancias)


g = Grafo(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
