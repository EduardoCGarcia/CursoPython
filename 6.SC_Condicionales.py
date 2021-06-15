"""
SC Secuenciales
SC Condicionales (if, if-else, elif)
SC Secuenciales (while, for)
"""
import os
os.system('cls')

"""edad = int(input('Digite su edad: '))
if edad>=18:
    print('Eres mayor de edad')
else:
    print('Aun eres menor de edad')"""
"""n = int(input('Digite un nuemro entre 1 y 30: '))
if n>=0 and n<=10:
    print('Rango: [0-10]')
else:
    if n>10 and n<=20:
        print('Rango: [11-20]')
    else:
        if n>20 and n<=30:
            print('Rango: [21-30]')"""

n = int(input('Digite un nuemro entre 1 y 30: '))
if n>=0 and n<=10:
    print('Rango: [0-10]')
elif n>10 and n<=20:
    print('Rango: [11-20]')
elif n>20 and n<=30:
    print('Rango: [21-30]')

