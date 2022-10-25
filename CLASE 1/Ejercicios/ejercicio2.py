#Ana ha encontrado en casa de su abuelo un antiguo termómetro, que está graduado en grados Fahrenheit. Luego de mirar con atención, ve que el
#termómetro indica una temperatura de 78°F. Ana no sabe si el termómetro está funcionando mal, o se trata de una lectura correcta.
#Vamos a intentar ayudarla. Escribe un programa que pida una temperatura en grados Celsius y 
#que muestre esa temperatura en grados Fahrenheit. Y otro pida
#una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Celsius.
#Pista: la relación entre grados Celsius (C) y grados Fahrenheit (F) F = 1.8 * C + 32, y
#la relación entre grados Celsius (C) y grados Fahrenheit (F) es C = (F - 32) / 1.8

print("Ejercicio 2 Temperaturas")
print()
temperaturaC= float(input("Escriba una temperatura Celsius pasar a Fahranheit: "))
fara = (1.8 * temperaturaC) + 32
print("-----------")
print("Su valor en Fahranheit es ", fara)
print("-----------")
print()
temperaturaF= float(input("Escriba una temperatura Fahranheit pasar a Celsius: "))
print()
cel =  (temperaturaF-32) / 1.8
print("-----------")
print("Su valor en Fahranheit es ", cel)
print("-----------")
