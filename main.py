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

        clientes[codigo]={
            "nombre": nombre,
            "destinos": destinos
        }

 def Contar_viajes(lista,i=0,j=0):
     if i>=len(lista):
         return 0
     elif j>=len(lista[i]):
         return Contar_viajes(lista,i+1,0)
     else:
         return 1+Contar_viajes(lista,i,j+1)

def clientes_Destinos(clientes):
    max_destinos=-1
    clientes_mayor=""
    for codigo, datos in clientes.items():
        contador=0
        for _ in datos["destinos"]:
            contador=+1
        if contador>max_destinos:
            max_destinos=contador
            clientes_mayor=print(f"Codigo: {codigo}, Nombre: {datos['nombre']} Cantidad de destinos: {_[datos]['destinos']}")
