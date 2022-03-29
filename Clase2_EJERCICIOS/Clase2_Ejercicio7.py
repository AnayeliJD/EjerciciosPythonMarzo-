from random import randint  #Sintaxis de las importaciones de Python

zonaUsuario = int (input("¿En qué zona desea disparar?: "))
zonaPortero = randint(1,6) #se ubica el rango de los números, este incluye del 1 al 6

#randint(inicio,fin) números aleatorios
#random() sin parámetros hace un número aleatorio engtre 0.0 y 1.0
#randrange(inicio,fin,paso) igual aleatorio entre inicio y fin con un paso igual
#uniform(inicio,fin) genera un número aleatorio de tipo flotante


print("La zona cubierta por el portero es: ",zonaPortero)

if int(zonaUsuario)==int(zonaPortero):
    print("No ha sido un gol")
else:
    print("Gooool")    
