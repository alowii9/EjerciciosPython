#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

num1 = float(input('ingrese numero :'))
numResto = num1%2

if numResto == 0:
    print('su numero es PAR')
else:
    print('su numero es IMPAR')    