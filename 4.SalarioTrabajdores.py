import os
os.system('cls')
nombre=input('Nombre del trabajador: ')
horas=int(input('Numero de horas trabajadas: '))
ph=float(input('Pago por hora: '))
salario = horas*ph
print('El salario de %s es de: $%.2f'%(nombre,salario))


