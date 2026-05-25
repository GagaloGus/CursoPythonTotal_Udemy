from bs4 import BeautifulSoup
import requests


ENLACE = "https://fede-garay.vercel.app"
resultado = requests.get(ENLACE)
# print(resultado) # -> <Response [200]>

soup = BeautifulSoup(resultado.text, "lxml")
soup # -> HTML completo de la página
soup.select("title") # -> [<title>Fede Garay - Portafolio</title>]
soup.select("h2") # -> Lista de todos los h2 que hay en la pagina
soup.select("h2")[0].get_text() # -> Texto dentro del primer h2
soup.select("#videos h3") # -> Elementos h3 dentro del elemento con id "videos"

# for titulo in soup.select("#interviews h3"):
#     print(titulo.get_text())

# for etiqueta in soup.select("#videos a"):
#     print(etiqueta["href"]) # -> Imprime el 'enlace' de cada etiqueta dentro del elemento con id "videos"

# Descargar imagenes
imagenes = soup.select("img")
url_imagen = f"{ENLACE}{imagenes[0]['src']}" # -> 'enlace' completo de la imagen (https://fede-garay.vercel.app/img/fede.png)
nombre_imagen = url_imagen.split("/")[-1] # -> Nombre de la imagen (fede.png)
requests.get(url_imagen).content # -> Contenido binario de la imagen

foto = open(nombre_imagen, "wb") # -> Abre un archivo en modo escritura binaria
foto.write(requests.get(url_imagen).content) # -> Escribe el contenido binario
foto.close()

# Bucle que descarga todas las imagenes de la página
# for foto in soup.select("img"):
#     print(f"{ENLACE}{foto['src']}")
#     url_foto = f"{ENLACE}{foto['src']}"
#     nombre_foto = url_foto.split("/")[-1]
#     with open(nombre_foto, "wb") as archivo:
#         archivo.write(requests.get(url_foto).content)