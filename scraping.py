import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase, digits
import codecs
from time import strftime

#Archivo para registrar los animes abierto con UTF-8 para poder escribir caracteres especiales
with codecs.open("Animes.txt", "w", encoding="utf-8") as save:
    save.write(strftime("Fecha del registro: %d/%m/%Y\n\n"))

    searching = ascii_lowercase + digits #Letras y digitos para buscar
    for search in searching:
        print(search) #Conocer que tan avanzado se va en las posibles busquedas
        error = False #Control cuando no hay más páginas en una busqueda
        pag = 1 #Por cada busqueda resetear la página a 1

        while not error: #Mientras haya páginas
            data = requests.get("https://jkanime.net/buscar/" + str(search) + "/" + str(pag)) #Página
            soup = BeautifulSoup(data.text, "html.parser")

            animes = soup.find_all("div", {"class": "let-post"}) #Los animes están contenidos en div's con la clase let-post
            for anime in animes:
                try:
                    title = anime.find("h2").text
                    save.write(title+"\n")
                #Cuando en una página no hay animes se encuentra un aviso en un let-post
                #pero se muestra con <p> y no con <h2>,
                #cuando se quiera obtener el texto de <h2> devuelve un error ya que la busqueda devuelve None.
                #Esto significa que no hay más animes para una busqueda
                #Se sale del bucle y el error = True
                except:
                    error = True
                    break

            pag += 1 #Siguiente página
    save.close()
