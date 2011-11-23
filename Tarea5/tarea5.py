#!/usr/bin/python
archivo1 = open("cleanme.txt" , "r")
archivo2 = open("salida" , "w")

lista = []

for linea in archivo1:
    if linea.isspace():
        continue
    linea = linea.strip()
    lista.append(linea)

# Hacemos el cambio de Lista a Set para poder quitar duplicados
# Luego Cambiamos de Set a una nueva lista para ordenar el contenido
miSet = set(lista)
miNuevaLista = list(miSet)
miNuevaLista.sort()

# Imprime todo nuevamente...
for linea in miNuevaLista:
    print linea

archivo1.close()
archivo2.close()
