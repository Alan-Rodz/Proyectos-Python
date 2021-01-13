import pytube
 
url = input("Dame la url que quieres usar. El video sera descargado al escritorio.\n")

video = pytube.YouTube(url)

print("Aqui estan las opciones disponibles. Ingresa el numero de itag que quieres usar.")
for stream in video.streams:
  if "video" in str(stream) and "mp4" in str(stream):
    print(stream)

itag = input("Dame la iTag que quieres usar: \n")

stream = video.streams.get_by_itag(itag)
print("Descargando...")
stream.download(filename="videoDescargado")
print("Listo!")
