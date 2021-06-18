#Listas: Unidimencionales, Bidimencionales, Tridimencionales, Multidimencionales
import os
os.system('cls')
#UNIDIMENCIONALES
x=[1,2,3,4,5]

"""
Listas (mutables,indices)
Tuplas (inmutables,indices)
Conjuntos (no indices)
Diccionarios (no indices)
"""

"""
En Python las listas pueden ser de varios tipos de datos además de que también puede
contener otras listas con más datos.
Algo interesante de las listas en Python es que nos permite acceder a sus datos incluso
con posiciones negativas.
"""
#nombres=['Eduardo','Angel','Gonzalo','Erick','Estefany',25,15,True,[1,2,3]]
#print(x,type(x))
#print(x[0])
#print(nombres[-1])

#Tamaño de una lista
#print(len(nombres))

#Rangos
"""print(nombres[0:5]) #No incluye al 5
print(nombres[:5]) 
print(nombres[0:9]) 
print(nombres[:]) 
print(nombres[::2]) """
#print(nombres[::-1]) #Lo recorre del ultimo al primero
#print(nombres[-1:-5:-1])

#Lista de listas Bidimencional
"""m=[[1,2,3],[4,5,6],[7,8,9]]
print(m[0][0])
print(m[0][1])
print(m[0][2])"""

"""nombres=['Eduardo','Angel','Gonzalo','Erick','Estefany']
#Agregar datos a las listas (recordar que python es orientado a objetos)
print(nombres)
nombres.append('Juan')
print(nombres)
nombres.extend([1,2,3]) #Agrega otra lista al final de la lista actual
nombres.pop(3) #Elimina datos de la lista
print(nombres[::])"""

"""
Tuplas
Las tuplas se declaran con parentesis y no pueden ser modificadas
"""
nombres=('juan','Eduardo','Gonzalo','Martin')
print(nombres[0])