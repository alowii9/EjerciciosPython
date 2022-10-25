#Los tramos impositivos para la declaración de impuestos en un determinado país
#son los siguientes:

#Renta Tipo impositivo
#Menos de $ 10000 5%
#Entre $ 10000 y $ 20000 15%
#Entre $ 20000 y $ 35000 20%
#Entre $ 35000 y $ 60000 30%
#Más de $ 60000 45%

#Escribir un programa que pregunte al usuario el monto de sus ingresos anuales y
#muestre por pantalla el monto de impuestos a pagar.

ingresos = float(input('ingrese sus ingresos: '))

if ingresos<10000:
    print('debe pagar : ', ingresos*0.05)

elif ingresos> 10000 and ingresos<20000:
     print('debe pagar : ', ingresos*0.15)   

elif ingresos> 20000 and ingresos<35000:
     print('debe pagar : ', ingresos*0.20) 

elif ingresos> 35000 and ingresos<60000:
     print('debe pagar : ', ingresos*0.30) 
     
elif ingresos> 60000:
     print('debe pagar : ', ingresos*0.45)                 