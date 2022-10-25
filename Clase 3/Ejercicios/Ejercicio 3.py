#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.

num1 = float(input('ingrese el primer numero: '))
num2 = float(input('ingrese el segundo numero: '))

if num2 == 0:
    print('no se puede dividir entre ceros')
else:
    print('la division es: ', (num1/num2))    