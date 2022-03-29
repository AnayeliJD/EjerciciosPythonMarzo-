frase = "sloegwjbdkhfr jadrksg"
letra = "k"
cont = 0
print("Sokución Ejercicio 13")
for carac in frase:
    if carac==letra:
        cont+=1
if cont>0:
    print("La letra " + letra + " se encontró " + str(cont) + " veces.")
else:
    print("No se encontró la letra " + letra)


