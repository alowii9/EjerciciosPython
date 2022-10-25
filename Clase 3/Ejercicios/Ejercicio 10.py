#Un municipio ha licitado una obra, y necesita determinar cuál es la opción más
#económica de las tres presentadas. Escribir un programa qué solicite al
#funcionario a cargo los importes de cada una de las ofertas recibidas y muestre
#en la pantalla el menor de los tres.

oferta1 = float(input('ingrese primera oferta : '))
oferta2 = float(input('ingrese segunda oferta : '))
oferta3 = float(input('ingrese tercera oferta : '))

if oferta1 < oferta2 and oferta1 < oferta3:
     print('la oferta 1 es la mas baja')

elif oferta2 < oferta1 and oferta2 < oferta3:   
     print('la oferta 2 es la mas baja')

elif oferta3 < oferta1 and oferta3 < oferta2:   
     print('la oferta 3 es la mas baja')    

else: 
    print('Todas las ofertas son iguales')     


    
