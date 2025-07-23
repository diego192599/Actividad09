clientes={}
def registrarClientes():
    n=int(input("Ingrese la cantidad de clientes a registrar: "))
    for i in range(n):
        print(f"Cliente #{i+1}")
        codigo=input("Ingrese el codigo del cliente: ")
        nombre=input("Ingrese el nombre del cliente: ")
        while True:
            cantidad_Destinos=int(input("¿Cuantos destinos debe registrar? (1 a 5)"))
            if 1<=cantidad_Destinos<=5:
                break
            print("Debe ingresar al menos 1 a 5 destinos")
        destinos=[]
        for j in range(cantidad_Destinos):
            destino=input(f" Destino {i+1}")
            destinos.append(destino)

