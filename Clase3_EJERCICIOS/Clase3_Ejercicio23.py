listaPesos=[55,50,80,75]
suma=0
sumaAnterior=0

for i in range(len(listaPesos)-1):
    for j in range(len(listaPesos)-1):
        if i!=j:
            if listaPesos[i]+listaPesos[j]<150:
                print("La pareja",listaPesos[i],"y",listaPesos[j])
                sumaAnterior= listaPesos[i]+listaPesos[j]
                if sumaAnterior>suma:
                    suma=sumaAnterior
print("La suma mayor que se encontró es",suma)
        
