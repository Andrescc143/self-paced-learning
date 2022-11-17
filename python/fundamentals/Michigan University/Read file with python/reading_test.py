#Código para extraer información de un archivo de texto

file = open('Read file with python/test.txt')
print("El archivo posee las siguientes características\n", file)

#Para leer su contenido
texto = ""
count = 0
for line in file:
    line = line.rstrip()
    if 'What is' in line:
        print(line)
print("Numero de lineas: ",count)

"""
#Para leer todo el archivo en su totalidad
texto = file.read()
print(texto)"""
