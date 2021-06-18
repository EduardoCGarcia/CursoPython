#Conjuntos
import os
os.system('cls')
# Los conjuntos no tiene  indices, no tienen posiciones por lo tanto no usan corchetes
programacion={'Juan','Pedro','Maria','Diana'}
# No se pueden duplicar los datos
calculo={'Eduardo','Santiago','Pedro','Gonzalo','Gonzalo'}

"""print('Maria' in programacion)
print(calculo)"""

"""programacion.add('Carmen')
print(programacion)
programacion.remove('Carmen')
print(programacion)"""
"""del programacion   #Elimina variables
print(programacion)"""
"""programacion.clear() #Limpia toda la variable
print(programacion)"""
C2=programacion | calculo
C3=programacion & calculo
C4=programacion - calculo
C5=calculo - programacion
print('Union', C2)
print('Intersección', C3)
print('Resta', C4)
print('Resta', C5)