#Por motivos históricos, algunos países utilizan unidades de medida que
#pueden resultarnos extrañas. Un ejemplo de ello son los pies y las pulgadas,
#utilizados para medir longitudes. Un pie equivale a doce pulgadas y una pulgada son 2,54 cm.
#Escribir un programa que pida al usuario una longitud expresada en pies y pulgadas y que escriba esa longitud en centímetros.
#Pista: Tu programa necesita solicitar dos valores al usuario, uno para la cantidad de pies y otro para la cantidad de pulgadas.

print("Ejercicio 1 Medidas")
print()
longitudPie= float(input("Escriba un valor en pies: "))
print()
longitudPulgada= float(input("Escriba un valor en pulgadas: "))
print()
pie_cm =  (longitudPie*12)*2.54
pulgada_cm = longitudPulgada*2.54
print("-----------")
print("El valor de pies en cm es: ", pie_cm)
print("-----------")
print("El valor de pulgadas en cm es: ", pulgada_cm)
print("-----------")
print("Su suma es : ", (pie_cm+pulgada_cm))