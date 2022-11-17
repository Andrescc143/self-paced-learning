#Archivo para hacer ejercicios con Tuplas

#Es posible realizar asignaciones múltiples
(x, y, z) = (1, 2, "Hola")
#print(z)

#Comparaciones entre colecciones
#print((14, 100, 1) < (14, 10, 10))


#Organizar un diccionario
keyval = {'age':15, 'xaludo':'hola', 'valor':50}
keyval_1 = {'a':1, 'c':3, 'b':2,}
#print(sorted(keyval.items()))
#print(sorted(keyval_1.items()))

x = 1,2
#print(dir(x))

x = ['hola', 'prueba']
a = x[-2][:2]
#print(a)



str = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
words = str.split()
hour = words[-2][0:2]
print(hour)
