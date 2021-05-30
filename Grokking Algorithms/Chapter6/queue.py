from queue import Queue

# Inicializando el queue
q = Queue(maxsize=3)

# qsize() devuelve el tamaño maximo del queue
print(q.qsize())

# Agregando elementos al queue
q.put('a')
q.put('b')
q.put('c')

# q.full devuelve si el queue esta lleno o no
print("\nLleno: ", q.full())

# Removiendo elementos del queue con q.get
print("\nElementos removidos del queue")
print(q.get())
print(q.get())
print(q.get())

# q.empty() regresa si el queue esta vacio o no
print("\nVacio: ", q.empty())

q.put(1)
print("\nVacio: ", q.empty())
print("Lleno: ", q.full())

