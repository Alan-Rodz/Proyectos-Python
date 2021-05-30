

# Devuelve la subcadena comun mas larga entre X[0...m-1] y Y[0...n-1]
def LCSubStr(X, Y, m, n):

    # Creamos una tabla para guardar la longitud de los sufijos mas largos de las subcadenas.
    # LCSuff[i][j] contiene la longitud del sufijo comun mas largo entre X[] y Y[]
    # La primera fila y la primera columna no tienen significado lógico.

    # Tabla que al inicio esta llena de 0s
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

    # Variable para guardar la longitud de la subcadena comun mas larga
    resultado = 0

    # Llenamos la tabla desde abajo hacia arriba
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                resultado = max(resultado, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return resultado


X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'

m = len(X)
n = len(Y)

print('La longitud de la subcadena mas larga es: ',LCSubStr(X, Y, m, n))

