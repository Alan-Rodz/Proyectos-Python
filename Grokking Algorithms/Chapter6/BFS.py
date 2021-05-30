from collections import defaultdict

# Representa un grafo con una lista de adyacencia
class Grafo:

    # Constructor
    def __init__(self):

        # diccionario default para guardar el grafo
        self.grafo = defaultdict(list)

    # funcion para agregar una conexion al grafo
    def agregarConexion(self, u, v):
        self.grafo[u].append(v)

    # funcion para imprimir recorrido BFS de un grafo
    def BFS(self, s):

        # marcamos todos los vertices no-visitados
        visitado = [False] * (max(self.grafo) + 1)

        # queue para BFS
        queue = []

        # marcamos el nodo inicial como visitado y lo agregamos al queue
        queue.append(s)
        visitado[s] = True

        while queue:

            # removemos un vertice del queue y lo imprimimos
            s = queue.pop(0)
            print(s, end=" ")

            # Obtenemos todos los vertices adyacentes al vertice que acabamos de remover
            # Si un vertice adyacente no ha sido visitado, lo marcamos como visitado y lo agregamos al queue
            for i in self.grafo[s]:
                if visitado[i] == False:
                    queue.append(i)
                    visitado[i] = True

# Driver code


# Creamos un grafo
g = Grafo()
g.agregarConexion(0, 1)
g.agregarConexion(0, 2)
g.agregarConexion(1, 2)
g.agregarConexion(2, 0)
g.agregarConexion(2, 3)
g.agregarConexion(3, 3)

print("Recorrido BFS empezando en el vertice 2: ")
g.BFS(2)

