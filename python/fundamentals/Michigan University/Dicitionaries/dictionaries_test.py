#archivo para garabatear

#Crear un dictionario
stock = dict()
stock['money'] = 12
stock['DPR'] = 2
stock['RAPIDUS 231R-E'] = 25
#print(stock)

#Modificar valores
stock['DPR'] = stock['DPR'] + 5
#print(stock['DPR'])

#Creación alterna
keyva = {'age': 5, 'nombre': 'Camilo'}
#print(keyva['nombre'])

#Evitar errores debido a llaves inexistentes
ex = {'Cantidad': 5, 'Item': 9}
#print(ex)
#print(ex.get('llave', "No existe esta llave"))

#Diccionarios con ciclos
ex_1 = {'Cantidad': 5, 'Item': 9, 'nombre': 'Camilo', 'age': 5}
#for item in ex_1:
    #print(item)


#Extraer llaves/valores
ex_1 = {'Cantidad': 5, 'Item': 9, 'nombre': 'Camilo', 'age': 5}
llaves = list(ex_1.keys())
#print(llaves)

#Extraer cada par formado por llave y valor, para cada ítemp
ex_1 = {'Cantidad': 5, 'Item': 9, 'nombre': 'Camilo', 'age': 5}
pares = ex_1.items()
#print(pares)

#Usando lo anterior en un ciclo for:
ex_1 = {'Cantidad': 5, 'Item': 9, 'nombre': 'Camilo', 'age': 5}
pares = ex_1.items()
#for llave,valor in pares:
    #print("\nLlave: {}\nValor: {}".format(llave, valor))

#Manipular diccionarios con dictionaries comprehension
ex_1 = {'Cantidad': 5, 'Item': 9, 'nombre': 'Camilo', 'age': 5}
ex_2 = {value:key for key, value in ex_1.items()}
print(ex_2.items())
