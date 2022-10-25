#Actividad 9:
#Una tienda necesita elaborar una estadística que involucra la cantidad de
#artículos comprados y la edad de sus clientes. Escribir un programa que le solicite
#al cliente su edad y la guarde en una variable. Qué luego solicite la cantidad de
#artículos comprados y la guarde en otra variable.
#Finalmente, que muestre en pantalla un valor de verdad (True o False) que
#indique si el cliente es mayor de 18 años de edad y además compró más de 1
#artículo.

edad = float(input('Ingrese edad : '))
cantidadPro = float(input('Ingrese cantidad de productos comprados: '))

if edad<=0:
    print('edad no valida')
    
elif edad>18 and cantidadPro>1:
    print(True)
    
else:
    print(False)        



