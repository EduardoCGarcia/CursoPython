#Diccionarios 
# Los diccionarios son como los JSON en web
import os
os.system('cls')
# Alumnos = {'key':'value'}
alumno1 = {'nombre':'Juan',
            'edad':20,
            'carrera':'ICO'}
alumno2 = {'nombre':'Eduardo',
            'edad':25,
            'carrera':'ICO'}
"""print(Alumnos)
print('Numero de elementos del diccionario:',len(Alumnos),'\n\n')"""

alumnos = [alumno1,alumno2] #Lista de diccionarios 
for a in alumnos:
    print('{:<10s}{:<5d}{:<5s}'.format(a['nombre'],a['edad'],a['carrera']))

print(alumno1.get('nombre'))
print(alumno1.values())  #los valores
print(alumno1.keys())   #los keys
print(alumno1.items())  #una lista de tuplas 

"""Alumnos['edad']=22
print(Alumnos['nombre'])
print(Alumnos['edad'])"""
