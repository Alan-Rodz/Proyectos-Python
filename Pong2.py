#Hecho siguiendo un tutorial que puede ser encontrado en https://www.youtube.com/watch?v=XGf2GcyHPhc&t=2739s
#bounce.wav puede ser encontrado en este link https://mega.nz/#!lg0VCZ5J!RieIOzaSD3aembVCTumQVc6sSoULYqtC1tnbnGMUlBM
#bounce.wav no me pertenece

#Versión sencilla del juego Pong
import turtle
import winsound

#Crear una ventana
ventana = turtle.Screen()

#Darle un titulo a la ventana
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)

#Previene el que la ventana se actualice
ventana.tracer(0)

#Mantener conteo de los scores
score_a = 0
score_b = 0

#Barra A
barra_a = turtle.Turtle()
barra_a.speed(0)  # Velocidad de la animación
barra_a.shape("square")
barra_a.color("white")
barra_a.shapesize(stretch_wid=5, stretch_len=1)
barra_a.penup()  #Hace que la tortuga no dibuje mientras se mueva
barra_a.goto(-350, 0)

#Barra B
barra_b = turtle.Turtle()
barra_b.speed(0)  #Velocidad de la animación
barra_b.shape("square")
barra_b.color("white")
barra_b.shapesize(stretch_wid=5, stretch_len=1)
barra_b.penup()  # Hace que la tortuga no dibuje mientras se mueva
barra_b.goto(350, 0)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)  # Velocidad de la animación
pelota.shape("square")
pelota.color("white")
pelota.penup()  #Hace que la tortuga no dibuje mientras se mueva
pelota.goto(0, 0)
#Separar el movimiento de la pelota en 2 partes
pelota.dx = 0.3  #Cada que la pelota se mueve lo hace en 0.3 pixeles
pelota.dy = 0.3

#Pluma para los scores
pluma = turtle.Turtle()
pluma.speed(0)
pluma.color("white")
pluma.penup()
pluma.hideturtle()
pluma.goto(-20, 260)
pluma.write("Jugador A: 0 Jugador B: 0", align="center", font=("Courier", 24, "normal"))

#Funciones
def barra_a_arriba():
    y = barra_a.ycor()  #regresa la coordenada en Y
    y += 30
    barra_a.sety(y)  #haz que la Y sea la nueva Y


def barra_a_abajo():
    y = barra_a.ycor()
    y -= 30
    barra_a.sety(y)


def barra_b_arriba():
    y = barra_b.ycor()
    y += 30
    barra_b.sety(y)


def barra_b_abajo():
    y = barra_b.ycor()
    y -= 30
    barra_b.sety(y)


#Teclas
ventana.listen()

#Cuando el usuario presione "w", llama la función barra_a_arriba
ventana.onkeypress(barra_a_arriba, "w")
ventana.onkeypress(barra_a_abajo, "s")
ventana.onkeypress(barra_b_arriba, "Up")
ventana.onkeypress(barra_b_abajo, "Down")

#Loop del juego principal
while True:
    ventana.update()

    #Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #Bordes
    #Borde superior
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1  #Invierte la dirección de la pelota
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Borde inferior
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Borde derecho
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        score_a += 1
        pluma.clear()
        pluma.write("Jugador A: {} Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Borde izquierdo
    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        score_b += 1
        pluma.clear()
        pluma.write("Jugador A: {} Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Colisiones con las barras y la pelota
    #Barra derecha
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < barra_b.ycor() + 40 and pelota.ycor() > barra_b.ycor() - 40):
        pelota.setx(340)
        pelota.dx *= -1

    #Barra izquierda
    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < barra_a.ycor() + 40 and pelota.ycor() > barra_a.ycor() - 40):
        pelota.setx(-340)
        pelota.dx *= -1
