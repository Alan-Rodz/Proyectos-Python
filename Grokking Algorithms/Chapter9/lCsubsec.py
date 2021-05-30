# Subsecuencia: Que los caracteres esten en ambas palabras
# (El numero de letras en una secuencia que ambas palabras tienen en comun)

def lcs(X, Y):

    # obtenemos la longitud de los strings
    m = len(X)
    n = len(Y)

    # arreglod onde guardamos los valores
    L = [[None]*(n+1) for i in range(m+1)]

    # construimos el arreglo desde abajo hacia arriba
    # L[i][j] contiene la longitud de la subsecuencia mas larga entre X[0...i-1] y Y[0...j-1]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # L[m][n] es la respuesta
    return L[m][n]



X = "AGGTAB"
Y = "GXTXAYB"
print("La longitud de la subsecuencia mas larga es: ", lcs(X, Y))
