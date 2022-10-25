#Un comerciante necesita ayuda para calcular el importe de una venta que
#acaba de realizar. Dispone del monto neto, y necesita agregar el porcentaje
#correspondiente al IVA, es decir, sumarle al importe que tiene un 21% más. Para
#ello, realizar un programa que solicite al usuario el monto neto y le sume el 21%,
#mostrando el resultado final en la pantalla.
#Reto 1: utiliza una sola variable.
print("Ejercicio 4 SUMANDO IVA")
print()
print("-----------")
monto = float(input("Escriba el monto: ")) 
print("-----------")
print("Su valor con IVA es: ", (monto*0.21 + monto))
print("-----------")