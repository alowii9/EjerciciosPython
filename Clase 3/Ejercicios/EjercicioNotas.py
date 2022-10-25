print("Ejercicio Notas")
print()
nota = float(input("Escriba su nota: ")) 

if nota >=0 and nota <4:
    print("Desaprobado")
elif nota >=4 and nota <7:
        print("en proceso")
elif nota >=7 and nota <10:
         print("Aprobado")
elif nota == 10:
             print("Felicitacion")
else:
        print("Nota Incorrecta")
