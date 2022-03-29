anioInicial = 1500
anioFinal = 2022
print("Solución Ejercicio 11")
r = "Los años bisiestos entre "+str(anioInicial)+" y "+str(anioFinal)+ " son:\n "
for i in range(anioInicial,anioFinal):
    if(i%4==0 and i%100!=0) or i%400==0:
        r = r + str(i)+ " ,"
print(r)
