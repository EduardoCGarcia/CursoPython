#Tuplas
#Las tuplas son inmutables es decir no se pueden modificar
import os
os.system('cls')
t=(1,2,3)
#Todo lo que sabemos de listas es aplicable aquí pero no se pueden modificar
#Podemos convertir una tupla en una lista y también una lista en una tupla
lista=list(t)
lista.append(5)
print(lista)
t=tuple(lista)
print(t)
lista.pop() #Borra el ultimo elemento de la lista
lista.remove(1) #Borra un elemento en espesifico
print(lista)
del lista[1] #Borra un indice de la lista
print(lista)

