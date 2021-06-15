import os
import math
os.system('cls')
"""n = 1
while n <= 5:
    print('Mensaje')
    n = n+1"""
"""range(n,m,i)
n : indica desde donde comienza a contar
m : indica hasta donde debe de contar hasta n-1 
i : indica el incremento (de cuanto en cuano)"""
"""for n in range(2, 10, 2):
    print('mensaje', n)"""
n = 'si'
while n == 'si' or n == 'SI':
    a = int(input('Dame a: '))
    b = int(input('Dame b: '))
    c = int(input('Dame c: '))

    # Validando ecuacion cuadrática
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

    n = input('¿Desea resolver otra ecuacion? [si / no]: ')
