datos=[0,1,2,3,4]
print(datos)
datos2=[i for i in range(1,51)] #La lista se llena sola con los numeros del 1 al 5
print(datos2)

multiplosde5=[i for i in range(1,100) if i%5==0]
print(multiplosde5)


print(ord('A'))#codifo ascci
print(chr(65))#codigo ascci

ABCDARIO=[chr(i) for i in range(65,91)] #Recorriendo como numeros para imprimir el caracter
print(ABCDARIO)

#lista de listas 
#M=[i for j in range(1,6) for i in range(1,11)]
M=[[(i,j) for j in range(1,6)] for i in range(1,11)]
print(M)

#Diccionarios
d={i:i for i in range(1,51)}

print(d)



