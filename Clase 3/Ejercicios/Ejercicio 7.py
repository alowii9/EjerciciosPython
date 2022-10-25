#Escribir un programa para una sala con juegos para todas las edades y se necesita
#calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
#El programa debe preguntar al usuario la edad del cliente y mostrar el precio de
#la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y
#18 años debe pagar $ 200 y si es mayor de 18 años, $ 300.

edadCliente = int(input('Digite su edad: '))

if edadCliente < 0:
    print('Edad Incorrecta')

elif edadCliente < 4:
    print('El cliente pasa gratis')

elif edadCliente >=4 and edadCliente <= 18:   
    print('El Cliente debe abonar 200 pesos') 

elif  edadCliente > 18:
    print('El cliente debe abonar 300 pesos ')   