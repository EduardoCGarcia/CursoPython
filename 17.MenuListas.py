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
numcta = []
nombres = []
edades = []
carreras = []
promedios = []

while op != 6:
    os.system('cls')
    print(menu)
    op = int(input('Escoge una opción: '))
    if op == 1:
        os.system('cls')
        print('*** AGREGAR A UN ALUMNO ***\n')
        nombres.append(input('Nombre: '))
        carreras.append(input('Carrera: '))
        edades.append(int(input('Edad: ')))
        promedios.append(float(input('Promedio: ')))
        numcta.append(len(numcta)+1)
        input('Presione enter para continuar...')
    elif op == 2:
        os.system('cls')
        encontrado=False
        print('*** ELIMINAR A UN ALUMNO ***\n')
        buscado=int(input('Digite el numero de cuenta del alumno: '))
        for i in range(0,len(numcta)):
            if buscado==numcta[i]:
                encontrado=True
                break 
        if encontrado:
            numcta.pop(i)
            nombres.pop(i)
            edades.pop(i)
            carreras.pop(i)
            promedios.pop(i)
            input('Se elimino al alumno exitosamente, presione enter para continuar...')
        else:
            input('El alumno no existe, presione enter para continuar...')
    elif op == 3:
        os.system('cls')
        encontrado=False
        print('*** CONSULTAR A UN ALUMNO ***\n')
        buscado=int(input('Digite el numero de cuenta del alumno: '))
        for i in range(0,len(numcta)):
            if buscado==numcta[i]:
                encontrado=True
                break 
        if encontrado:
            print('{:<10d}{:<10s}{:<10s}{:<10}{:10.2f}'.format(
                numcta[i],nombres[i], carreras[i], edades[i], promedios[i]))
            input('Presione enter para continuar...')
        else:
            input('El alumno no existe, presione enter para continuar...')
    elif op == 4:
        os.system('cls')
        encontrado=False
        print('*** ACTUALIZAR A UN ALUMNO ***\n')
        buscado=int(input('Digite el numero de cuenta del alumno: '))
        for i in range(0,len(numcta)):
            if buscado==numcta[i]:
                encontrado=True
                break
        if encontrado:
            opc2=None
            while opc2!=5:
                menu2="""
MENU ACTUALIZACIONES
1. Nombre 
2. Edad 
3. Carrera 
4. Promedio
5. Regresar
"""
                print(menu2)
                opc2=int(input('Que deseas modificar: '))
                if opc2==1:
                    nombres[i]=input('Dame el nuevo nombre: ')
                elif opc2==2:
                    edades[i]=int(input('Dame la nueva edad: '))
                elif opc2==3:
                    carreras[i]=input('Dame la nueva carrera: ')
                elif opc2==4:
                    promedios[i]=int(input('Dame el nuevo promedio: ')) 
                elif opc2==5:
                    input('Presione enter para continuar...')
        else:
            input('El alumno no existe, presione enter para continuar...')  
    elif op == 5:
        os.system('cls')
        # No importa que lista recorramos ya que todos tienen el mismo tamaño
        for i in range(0, len(nombres)):
            print('{:<10d}{:<10s}{:<10s}{:<10}{:10.2f}'.format(
                numcta[i],nombres[i], carreras[i], edades[i], promedios[i]))
        input('Presione enter para continuar...')
    elif op == 6:
        input('Fue un placer atenderle, presione enter para salir...')
    else:
        input('La opción no es valida, presione enter para volver a intentar...')
