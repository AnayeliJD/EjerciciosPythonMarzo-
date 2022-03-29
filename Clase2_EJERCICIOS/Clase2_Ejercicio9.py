a= 6
b= 4

print("La ecuación es: ",a,"x + ",b,"= 0")

if a==0==b:
    r = "Todos los numeros so solución"
elif a==0:
    r = "No existe solución"
else:
    r = "La única solución es: " + str(-b/a)
print(r)