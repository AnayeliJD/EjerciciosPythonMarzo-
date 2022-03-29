from random import randint
ganadasUsuario = 0
ganadasMaquina = 0

def ppt(op):
    if op==1:
        r="piedra"
    elif op==2:
        r="papel"
    elif op==3:
        r="tijera"
    return r
    

while ganadasUsuario<3 and ganadasMaquina<3:   
    opUsuario = int(input("Ingrese una opción:\n1.-Piedra \n2.-Papel \n3.-Tijera \n "))
    if opUsuario>3 or opUsuario<1:
        continue
    opMaquina = randint(1,3)
    print("Usted eligió: ",opUsuario)
    print("La máquina eligió: ",opMaquina)
    if(opUsuario==1 and opMaquina==3) or (opUsuario==2 and opMaquina==1) or (opUsuario==3 and opMaquina==2):
        print("Gana el usuario: ")
        ganadasUsuario+=1
    elif opUsuario==opMaquina:
        print("Es un empate")
    else:
        print("Gana la Máquina")
        ganadasMaquina+=1




