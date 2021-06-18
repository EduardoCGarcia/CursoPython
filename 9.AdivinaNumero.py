import random  # Libreria para gerenar los numeros aleatorios
import os

os.system('cls')

num = random.randint(1, 10)
n = 0
i = 1
while i <= 3:
    n = int(input('Intenta adivinar que numero estoy pensando entre el 1 y el 10: '))
    if n == num:
        print('¡GENIAL LO HICISTE!')
        break
    elif n < num:
        print('No, mas grande')
    else:
        print('No, mas pequeño')
    i = i+1

if i != 3:
    print('El numero en el que pense es: ', num)
