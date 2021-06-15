
# Este menu es una practica con lo viso hasta while y for
import math
import os

op = 'si'
while op != 4:
    os.system('cls')
    print('     MENU')
    print('1. Area de triangulo')
    print('2. Ecuacion cuadratica')
    print('3. Salario de trabajador')
    print('4. Salir')
    op = int(input('Digite una opcion: '))
    if op == 1:
        a = int(input('Dame el primer lado: '))
        b = int(input('Dame el segundo lado: '))
        c = int(input('Dame el tercer lado: '))
        s = (a + b + c)/2
        result = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print('El area del triangulo con los lados: %d,%d,%d tiene un area de %.2f' % (
            a, b, c, result))
    elif op == 2:
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
    elif op == 3:
        nombre = input('Nombre del trabajador: ')
        horas = int(input('Numero de horas trabajadas: '))
        ph = float(input('Pago por hora: '))
        salario = horas*ph
        print('El salario de %s es de: $%.2f' % (nombre, salario))
    else:
        print('Fue un placer atenderle')
    input('Presione enter para continuar...')
