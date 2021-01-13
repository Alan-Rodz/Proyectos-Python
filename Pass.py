#Generador de contraseñas con puro ASCII
import random
import sys

todoASCII = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
            "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", '"', "#", "$", "%", "&", "(", ")", "*", "+",
            ",", "-", ".", ":", ";", "?", "@", "[", "]", "^", "_", "~", "{", "}", "|"]

size = input("De que tamaño quieres que sea tu contraseña?\n")

while(True):
    decision = input("Ingresa 1 para generar una contraseña aleatoria nueva o 0 para salir:\n")
    password = ""
    if(decision == "1"):
        for i in range(int(size)):
            password = password + random.choice(todoASCII)
    elif(decision == "0"):
        sys.exit()
    print(password)




