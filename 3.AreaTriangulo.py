import math
import os

os.system('cls')
a = int(input('Dame el primer lado: '))
b = int(input('Dame el segundo lado: '))
c = int(input('Dame el tercer lado: '))

"""
Operadores:
Aritmeticos: +,-,*,/,//(Solo el valor entero),%(el residuo),**(Potencia)
Relacionales: >,<,<=,>=,==,!=,
Logicos: and,or,not
Especiales
"""
s = (a + b +c)/2 
result = math.sqrt(s*(s-a)*(s-b)*(s-c))

print('El area del triangulo con los lados: %d,%d,%d tiene un area de %.2f'%(a,b,c,result))