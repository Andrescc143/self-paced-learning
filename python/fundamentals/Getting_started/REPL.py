#Se importan librerías
import sys
from urllib.request import urlopen

#"http://sixty-north.com/c/t.txt"
#Función a trabajar
def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

#Función complementaria
def print_words(story_words):
    for word in story_words:
        print(word)

#Para ejecutar en el REPL o CMD correctamente
def main(url):
    words = fetch_words(url)
    print_words(words)

#Ejecutamos main solo en caso de que el script se use desde la línea de comandos
if __name__ == '__main__':
    main(sys.argv[1])
