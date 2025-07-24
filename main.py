clientes = {}

def registrarClientes():
    n = int(input("Ingrese la cantidad de clientes a registrar: "))
    for i in range(n):
        print(f"\nCliente #{i+1}")
        codigo = input("Ingrese el código del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")

        while True:
            cantidad_Destinos = int(input("¿Cuántos destinos debe registrar? (1 a 5): "))
            if 1 <= cantidad_Destinos <= 5:
                break
            print("Debe ingresar entre 1 y 5 destinos.")

        destinos = []
        for j in range(cantidad_Destinos):
            destino = input(f"Destino {j+1}: ")
            destinos.append(destino)

        clientes[codigo] = {
            "nombre": nombre,
            "destinos": destinos
        }

def Contar_viajes(lista, i=0, j=0):
    if i >= len(lista):
        return 0
    elif j >= len(lista[i]):
        return Contar_viajes(lista, i + 1, 0)
    else:
        return 1 + Contar_viajes(lista, i, j + 1)

def clientes_Destinos(clientes):
    max_destinos = -1
    cliente_mayor = None

    for codigo, datos in clientes.items():
        contador = len(datos["destinos"])
        if contador > max_destinos:
            max_destinos = contador
            cliente_mayor = (codigo, datos['nombre'], contador)

    if cliente_mayor:
        print("\nCliente con más destinos:")
        print(f"Código: {cliente_mayor[0]}")
        print(f"Nombre: {cliente_mayor[1]}")
        print(f"Cantidad de destinos: {cliente_mayor[2]}")
    else:
        print("No hay clientes registrados.")

def Mostrar(clientes):
    print("\n=== Lista de clientes registrados ===")
    for codigo, datos in clientes.items():
        print(f"Código : {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print("Destinos: ", end="")
        contados=0
        total=len(datos['destinos'])
        for destinos in datos['destinos']:
            print(destinos,end="")
            contados+=1
            if contados< total:
                print("", end="")
        print()

def total_destinos(clientes):
    lisa_datos=[]
    for datos in clientes.values():
        lisa_datos.append(datos['destinos'])
    total=Contar_viajes(lisa_datos)
    print(f"\n Total de viajes realizados entre todo los clientes es {total}")


while True:
    print("\n== Menú ==")
    print("1. Registrar clientes")
    print("2. Mostrar clientes")
    print("3. Cliente con más destinos")
    print("4. Total de destinos registrados")
    print("5. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        registrarClientes()
    elif opcion == 2:
        Mostrar(clientes)
    elif opcion == 3:
        clientes_Destinos(clientes)
    elif opcion == 4:
        total_destinos(clientes)
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Debe seleccionar una opción válida. Intente nuevamente.")
