#Para tributar un determinado impuesto se debe ser mayor de 18 años y tener
#unos ingresos mensuales iguales o superiores a $ 30000 . Escribir un programa
#que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla
#si el usuario tiene que tributar o no.

print("Ejercicio 5 Impuestos")
print()
edad = float(input("Escriba su edad: ")) 
ingresos = float(input("Escriba sus ingesos: ")) 
print("-----------")
if edad >= 18 and ingresos >=30000:
    print("Puede tributar")
else:
    print("No puede tributar")   

