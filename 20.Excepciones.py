import os
os.system('cls')
lista=[2,3]
#Atrapar errores
# Todo lo que puede generar un error debe ir dentro de try
"""try:
    # ValueError: se genera cuando quiere convertir una cadena en un entero
    num=int(input('Dame un numero: '))
    print(num)
    print(5/num)
    print(lista[10])
except ValueError as e: #e es un obejeto de la clase ValueError
    print(e.__str__) #<method-wrapper '__str__' of ValueError object at 0x000001FF890AC4A0>
    print('El dato no es valido')
except ZeroDivisionError as e: #e es un obejeto de la clase ValueError
    print(e.__str__) #<method-wrapper '__str__' of ValueError object at 0x000001FF890AC4A0>
    print('La division entre cero no es posible')
except:
    print('Algo salió mal')"""
error=False
while not error:
    try:
        num=int(input('Dame un numero: '))
        print(num)
        error=True
    except ValueError as e: #e es un obejeto de la clase ValueError
        print('El dato no es valido')