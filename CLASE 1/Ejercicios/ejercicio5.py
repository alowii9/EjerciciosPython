#Un fabricante de cámaras de acción indica en sus publicidades la duración de
#la batería de sus productos utilizando como unidad el segundo. Por ejemplo, el
#modelo “Pro 4K” tiene una batería cuya duración es, según el manual, de 8000 segundos.
#Realiza un programa que pida una cantidad de segundos y que
#escriba cuántas horas, minutos y segundos contiene ese lapso de tiempo.
print("Ejercicio 5 cantidad de horas")
print()
segundo = float(input("Escriba una cantidad en segundos: ")) 
print("-----------")
print()
hora=segundo/3600
minuto=segundo/60

print("Su valor en horas es :  ", hora)
print("-----------")
print("Su valor en minutos es :  ", minuto)
print("-----------")
print("Su valor en segundos es :  ", segundo)
print("-----------")

