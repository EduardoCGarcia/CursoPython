import os
os.system('cls')

def mensaje():
    print('mensaje')
mensaje()

def funcionregresa():
    return 'Cadena de regreso'
cadena=funcionregresa()
print(cadena)

def mostrarx(x):
    print('El valor de x es: ',x)
mostrarx(20)

def mult(x,y):
    return x*y
print('El resultado de la multiplicacion es: ',mult(5,2))

def alumno():
    nombre='Eduardo'
    edad=21
    promedio=9.5
    return nombre,edad,promedio
[nom,ed,prom]=alumno()
print('Nombre: {:<10s} Edad: {:<5d} Promedio: {:<5.2f}'.format(nom,ed,prom))

def suma(n1,n2,n3,n4,n5=10): #Los que se igualan a 0 son opcionales los otros son obligatorios
    return n1+n2+n3+n4+n5
print(suma(1,2,3,4))

def suma2(x,*args): #Los que se igualan a 0 son opcionales los otros son obligatorios
    print(args)
    s=x
    for i in args:
        s=s+i
    return s
print(suma2(5,6,6,6,5,5,5,54,4,4,8,5,9,4,5))

def alumno2(**kwargs):
    print(kwargs)
alumno2(nom='Eduardo',edad=20)#Estos datos los convierte en un diccionario