#Este programa imprime en consola el proceso de las Torres de Hanoi paso por paso, dibujándolas en consola

import time
from os import system, name
import sys

#Para la versión lenta del programa, descomentar la línea "time.sleep(1)" en la función "imprimir"

def Hanoi(filas, src, dst, tmp):
    #Devuelve la lista de movimientos entre torres (lo que sea que haya en 1 a 3, etc)
	if filas <= 0:
		pass
	else:
		for h in Hanoi(filas-1, src, tmp, dst):
			yield h
		yield (src, dst)
		for h in Hanoi(filas-1, tmp, dst, src):
			yield h

def generadorPiramides(numeroDeFilas):
    matrizGenerada = []
    for j in range(numeroDeFilas):
        if j == 0:
            matrizGenerada.append(("*"*(j+1)).center(2*numeroDeFilas-1, " "))
        elif j == 1:
            matrizGenerada.append(("*"*3).center(2*numeroDeFilas-1, " "))
        else:
            matrizGenerada.append(("*"*(2*j+1)).center(2*numeroDeFilas-1, " "))

    return matrizGenerada

def imprimir(A, B, C, filas, verdad):
    #Generamos copias de las matrices, las hacemos de la misma dimensión que las demás, luego las exponemos
    Ax = A.copy()
    Bx = B.copy()
    Cx = C.copy()

    while len(Ax) < filas:
        Ax.insert(0, " ".center(2*filas-1, " "))

    while len(Bx) < filas:
        Bx.insert(0, " ".center(2*filas-1, " "))

    while len(Cx) < filas:
        Cx.insert(0, " ".center(2*filas-1, " "))

    #Imprimimos la primera linea de cada arreglo al mismo tiempo
    for i in range(filas):
        print(Ax[i] + "    " + Bx[i] + "    " + Cx[i])
    print("------------------------------------------------------------------------------------------------------")
    #time.sleep(1)
    if verdad == True:
        limpiar()
    else:
        pass

def limpiar():
    if name == 'nt':
        _ = system('cls')

def ejecutarPrograma(solucion):
    for i in solucion:
        if i == (1, 2):
            print("------------------------------------------------------------------------------------------------------")
            print("1 a 2")
            print("------------------------------------------------------------------------------------------------------")
            #Modificamos las 3 Piramides
            B.insert(0, A[0])
            A.pop(0)
            imprimir(A, B, C, filas, True)

        elif i == (1, 3):
            print("------------------------------------------------------------------------------------------------------")
            print("1 a 3")
            print("------------------------------------------------------------------------------------------------------")
            #Modificamos las 3 piramides
            C.insert(0, A[0])
            A.pop(0)
            imprimir(A, B, C, filas, True)

        elif i == (2, 1):
            print("------------------------------------------------------------------------------------------------------")
            print("2 a 1")
            print("------------------------------------------------------------------------------------------------------")
            #Modificamos las 3 piramides
            A.insert(0, B[0])
            B.pop(0)
            imprimir(A, B, C, filas, True)

        elif i == (2, 3):
            print("------------------------------------------------------------------------------------------------------")
            print("2 a 3")
            print("------------------------------------------------------------------------------------------------------")
            #Modificamos las 3 piramides
            C.insert(0, B[0])
            B.pop(0)
            imprimir(A, B, C, filas, True)

        elif i == (3, 1):
            print("------------------------------------------------------------------------------------------------------")
            print("3 a 1")
            print("------------------------------------------------------------------------------------------------------")
            #Modificamos las 3 piramides
            A.insert(0, C[0])
            C.pop(0)
            imprimir(A, B, C, filas, True)

        elif i == (3, 2):
            print("------------------------------------------------------------------------------------------------------")
            print("3 a 2")
            print("------------------------------------------------------------------------------------------------------")
            #Modificamos las 3 piramides
            B.insert(0, C[0])
            C.pop(0)
            imprimir(A, B, C, filas, True)
    print("------------------------------------------------------------------------------------------------------")

def generarSolucion(filas):
    solucion = []
    for h in Hanoi(filas,1,3,2):
        solucion.append(h)
    return solucion

def obtenerFilas():
    filas = input("Dame el numero de filas (no se permiten caracteres).\n(El número máximo antes de abarcar demasiada memoria es 996, pero tomará mucho tiempo):\n")
    try:
        filas = int(filas)
    except:
        print("QUE NO SE PERMITEN CARACTERES")
        sys.exit()
    if filas < 1:
        print("No se permiten numeros negativos ni tampoco el cero")
        sys.exit()
    return filas

#Obtenemos las filas, generamos las piramides base, generamos la solucion, y ejecutamos el programa.
filas = obtenerFilas()
A = generadorPiramides(filas)
B = []
C = []
solucion = generarSolucion(filas)
ejecutarPrograma(solucion)
imprimir(A, B, C, filas, False)
