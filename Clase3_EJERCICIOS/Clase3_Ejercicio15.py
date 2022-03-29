n = 60
x = 8

def vasos(n,x):
    total = 0
    while n>=x:
        reciclados = n//x
        restantes = n%x
        total += reciclados
        n = reciclados + restantes
        print("N:",n,"\nReciclados:",reciclados,"sobran:",restantes,"\nTotal reciclados",total)
    return total

vasos(n,x)