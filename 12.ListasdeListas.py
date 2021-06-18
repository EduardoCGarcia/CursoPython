import os
os.system('cls')

"""lista = [[1,2,3,4,5],[6,7,8],[10,11,12,'juan']]
for i in lista:     #Recorre la lista llamada lista
    for j in i:     #recorre los elementos de cada sublista de la lista
        #print(j,end=' ')
        print("{0:<10}".format(j), end='') # que imprima [j] que es el valor
        #El simbolo < indica que olo esta jistificando a la izquierda
        #El numero despues de : significa el espacio que se da entre valores
    print() #imprime el salto de linea"""


"""for i in range(0,len(lista)):
    for j in range(0,len(lista[i])):
        print(lista[i][j], end=' ')
    print()"""


# Llenar del teclado

r = 3 #Renglones
c = 3 #Columnas
lista=[]
for i in range(0,r):
    lista.append([]) #Le estoy diciendo que es una lista de listas
    for j in range(0,c):
        lista[i].append(int(input('Dame un numero: ')))
        
for i in lista:     #Recorre la lista llamada lista
    for j in i:     #recorre los elementos de cada sublista de la lista
        #print(j,end=' ')
        print("{0:<10}".format(j), end='') # que imprima [j] que es el valor
        #El simbolo < indica que olo esta jistificando a la izquierda
        #El numero despues de : significa el espacio que se da entre valores
    print() #imprime el salto de linea"""

print()

for i in range(0,len(lista)):
    for j in range(0,len(lista[i])):
        print("{0:<10}".format(lista[i][j]), end='')
    print()