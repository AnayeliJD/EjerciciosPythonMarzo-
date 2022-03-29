altura = 5
espacio = altura
carac = 1
print("Solución Ejercicio 12")
for i in range(altura):
    for j in range(espacio):
        print("  ",end="")
        #en el rango puede ir el "caracter" como parámetro
    for k in range((i*2+1)):
        print("* ",end="")
    #después de espacio se incrementaría en 2 la variable caracter    
    espacio-=1
    print()