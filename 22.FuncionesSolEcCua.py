import os,math
os.system('cls')

def solucion(a,b,c):
    if a != 0:
        if 4*a*c <= math.pow(b, 2):
            x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
            x2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
            print('X1 = ', x1)
            print('X2 = ', x2)
        else:
            print('El resultado es imaginario')
    else:
        print('No es una ecuacion cuadratica')

a = int(input('Dame a: '))
b = int(input('Dame b: '))
c = int(input('Dame c: '))

solucion(a,b,c)
