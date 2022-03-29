from random import randint
def llenarSec(n):
    lista = []
    for i in range(1,n+1):
        lista+=[i]
    return lista


def llenarAle(n):
    lista=[]
    num = randint(1,n)
    lista+=[num]
    for i in range(1,n):
        while num in lista:
            num = randint(1,n)
        lista+=[num]
    return lista


listaA = llenarSec(10)
listaB = llenarAle(10)
print("Lista 1")
print(listaA)
print("Lista 2")
print (listaB)

print()
print("Resultados Oficiales")
for i in range(len(listaA)):
    print("La persona:",listaA[i],"es pareja con:",listaB[i])