correctos = int(input("Ingrese el número de aciertos: "))
errores = int(input("Ingrese el número de errores: "))
total= correctos + errores
PCorrecto = (100/total)*correctos
PErrores = (100/total)*errores
print("El puntaje final de la evaluación es: " + str(correctos) + "/" + str(total)) 
print("El porcentaje de aciertos es: %.2f y el porcentaje de errores de: %.2f"%(PCorrecto, PErrores))