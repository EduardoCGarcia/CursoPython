import os
os.system('cls')

menu = """
        MENU (CRUD)
        1.Altas (C)
        2.Bajas (D)
        3.Consultas (R)
        4.Actualizar (U)
        5.Reportes (R)
        6.Sair
        """
op = None

alumnos= []

while op != 6:
    os.system('cls')
    print(menu)
    op = int(input('Escoge una opción: '))
    if op == 1:
        os.system('cls')
        print('*** AGREGAR A UN ALUMNO ***\n')
        a={} #Creamos el diccionario vacio
        """ejemplo={
            'id':1,
            'nombre':'Eduardo',
            'edad':15
        }"""
        a['id']=(len(alumnos)+1) #agregamos el atributo llamado id
        a['nombre']=input('Nombre: ')
        a['edad']=int(input('Edad:'))
        a['carrera']=input('Carrera: ')
        a['promedio']=float(input('Promedio: '))
        alumnos.append(a)
        input('Presione enter para continuar...')
    elif op == 2:
        os.system('cls')
        encontrado=False
        indice=-1 #  Es necesario llevar el indice de la lista
        print('*** ELIMINAR A UN ALUMNO ***\n')
        buscado=int(input('Digite el numero de cuenta del alumno: '))
        for i in alumnos: #i lleva los valores de la lista no el indice de la lista
            indice+=1
            if buscado==i['id']:
                encontrado=True
                break 
        if encontrado:
            alumnos.pop(indice)
            input('Se elimino al alumno exitosamente, presione enter para continuar...')
        else:
            input('El alumno no existe, presione enter para continuar...')
    elif op == 3:
        os.system('cls')
        encontrado=False
        print('*** CONSULTAR A UN ALUMNO ***\n')
        buscado=int(input('Digite el numero de cuenta del alumno: '))
        for i in alumnos: #i lleva los valores de la lista no el indice de la lista
            if buscado==i['id']:
                encontrado=True
                break 
        if encontrado:
            print('ID: {:<10d} Nombre: {:<10s} Carrera: {:<10s} Edad: {:<10d} Promedio: {:10.2f}'.format(
                i['id'],i['nombre'], i['carrera'], i['edad'], i['promedio']))
            input('Presione enter para continuar...')
        else:
            input('El alumno no existe, presione enter para continuar...')
    elif op == 4:
        os.system('cls')
        encontrado=False
        print('*** ACTUALIZAR A UN ALUMNO ***\n')
        buscado=int(input('Digite el numero de cuenta del alumno: '))
        for i in alumnos: #i lleva los valores de la lista no el indice de la lista
            if buscado==i['id']:
                encontrado=True
                break 
        if encontrado:
            i['nombre']=input('Nombre: ')
            i['edad']=int(input('Edad:'))
            i['carrera']=input('Carrera: ')
            i['promedio']=float(input('Promedio: '))
            input('Presione enter para continuar...')
        else:
            input('El alumno no existe, presione enter para continuar...')
    elif op == 5:
        os.system('cls')
        for i in alumnos:
            print('ID: {:<10d} Nombre: {:<10s} Carrera: {:<10s} Edad: {:<10d} Promedio: {:10.2f}'.format(
                i['id'],i['nombre'], i['carrera'], i['edad'], i['promedio']))
        input('Presione enter para continuar...')
    elif op == 6:
        input('Fue un placer atenderle, presione enter para salir...')
    else:
        input('La opción no es valida, presione enter para volver a intentar...')
