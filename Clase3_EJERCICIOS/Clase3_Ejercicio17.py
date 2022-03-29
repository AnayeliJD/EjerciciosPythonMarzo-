saldo = 0
op = 0

while (op!=3):
    op=int(input("Ingrese la opción que requiera realizar:\n1.-Depósito \n2.-Retiro \n3.-Salir \n "))
    if op<0 or op>3:
        print("Opción no válida")
    if op==1:
        cant = float(input("Ingrese la cantidad que requiera despositar: "))
        saldo+=cant
    elif op==2:
        cant=float(input("Ingrese la cantidad que vaya a retirar: "))
        if cant>saldo:
            print("No puede retirar esa cantidad")
        else:
            saldo-=cant
    elif op==3:
        print("Saliendo......")

