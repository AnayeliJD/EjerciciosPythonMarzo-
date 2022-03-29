lista1 = ["a","b","c","d","e"]
lista2 = ["c","e","f","t","g"]
listaGlobal= []
lSolo1=[]
lSolo2=[]
lAmbas=[]

listaGlobal= lista1+lista2

for palabra in lista1:
    if palabra in lista2:
        lAmbas = lAmbas + [palabra]
    else: 
        lSolo1= lSolo1 + [palabra]

for palabra in lista2:
    if palabra not in lAmbas:
        lSolo2= lSolo2+[palabra]
print("Lista 1")
print(lista1)
print("Lista 2")
print(lista2)
print("Lista Total")
print(listaGlobal)
print("Solo valores lista 1")
print(lSolo1)
print("Solo valores lista 2")
print(lSolo2)
print("Valores de las 2 listas")
print(lAmbas)

