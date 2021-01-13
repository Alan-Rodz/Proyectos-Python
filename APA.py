#Generador de citas APA
def generarCita(decision):
    if(decision == "1"):
        autor = input("Autor(es): ")
        año = input("Año de publicacion: ")
        titulo = input("Titulo del libro: ")
        lugar = input("Lugar de publicacion: ")
        editorial = input("Editorial: ")
        print(autor + "." + " (" + año + "). " + titulo +
          ". " + lugar + ": " + editorial + ".")

    elif(decision == "2"):
        autor = input("Autor(es): ")
        fecha = input("Fecha: ")
        tituloArticulo = input("Titulo del Articulo: ")
        nombreRevista = input("Nombre de la revista: ")
        volumen = input("Volumen: ")
        paginas = input("Paginas: ")
        print(autor + "." + " (" + fecha + "). " + tituloArticulo +
          ". " + nombreRevista + ", " + volumen + ", " + paginas + ".")

    elif(decision == "3"):
        autor = input("Autor(es): ")
        año = input("Año de publicacion: ")
        tituloArticulo = input("Titulo del articulo: ")
        tituloPeriodico = input("Titulo del periódico: ")
        paginas = input("Páginas: ")
        print(autor + "." + " (" + año + "). " + tituloArticulo +
          ". " + tituloPeriodico + ", " + paginas + ".")

    elif(decision == "4"):
        autor = input("Autor(es): ")
        año = input("Año de publicacion: ")
        tituloArticulo = input("Titulo del articulo: ")
        nombreEnciclopedia = input("Nombre de la enciclopedia: ")
        volumen = input("Volumen: ")
        paginas = input("Paginas: ")
        lugarPublicacionEnciclopedia = input(
        "Lugar de publicación de la enciclopedia: ")
        editorial = input("Editorial: ")
        print(autor + "." + " (" + año + "). " + tituloArticulo + ". En " + nombreEnciclopedia +
          " ("+volumen+", "+paginas+"). " + lugarPublicacionEnciclopedia + ": " + editorial + ".")

    elif(decision == "5"):
        autor = input("Autor(es): ")
        año = input("Año de publicacion: ")
        titulo = input("Titulo del capítulo: ")
        nombre = input("Nombre del libro: ")
        paginas = input("Páginas: ")
        lugarPublicacion = input("Lugar de publicación del libro: ")
        editorial = input("Editorial: ")
        print(autor + "." + " (" + año + "). " + titulo + ". " + "En " +
          nombre + "("+paginas+"). " + lugarPublicacion+":" + editorial + ".")

    elif(decision == "6"):
        autor = input("Autor(es): ")
        año = input("Año de publicacion: ")
        titulo = input("Titulo del artículo: ")
        fecha = input("Fecha de recuperación del documento: ")
        asociacion = input("Asociación que publica el artículo: ")
        url = input("URL: ")
        print(autor + "." + " (" + año + "). " + titulo + ". " +
          fecha + ", de " + asociacion+". Sitio web: " + url)

    elif(decision == "7"):
        autor = input("Autor(es): ")
        fecha = input("Fecha: ")
        titulo = input("Titulo del artículo: ")
        nombrePoR = input("Nombre del periódico o revista: ")
        volumen = input("Volumen: ")
        paginas = input("Páginas: ")
        fechaBD = input(
        "Fecha en que se obtuvo la información de la base de datos: ")
        nombreBD = input(
        "Nombre de la base de datos de la cual se obtuvo la información: ")
        print(autor + "." + " (" + fecha + "). " + titulo + ". " + nombrePoR + ", " +
          volumen + ", " + paginas + ". " + fechaBD+", De la base de datos " + nombreBD+".")

    else:
        print("Opción inválida.")

while True:
    print("¿Qué vas a citar?\n1.Si tu fuente es un Libro.\n2.Si tu fuente es un artículo de Revista.\n3.Si tu fuente es un artículo de Periódico.\n4.Si tu fuente es un artículo de Enciclopedia.\n5.Si tu fuente es un artículo o capítulo de un Libro.\n6.Artículo de Página Web.\n7.Si tu fuente es el artículo de un Periódico, un Journal o Revista en una Base de Datos.\n")
    print("------------------------------")
    decision = input("Decisión: ")
    generarCita(decision)
    print("------------------------------")
