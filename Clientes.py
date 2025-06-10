class Cliente:
    def __init__(self, id, nombre, email, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def mostrar(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}")


clientes = []

def agregar_cliente():
    id = input("ID del cliente: ")
    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    cliente = Cliente(id, nombre, email, telefono)
    clientes.append(cliente)
    print("Cliente agregado.\n")

def mostrar_clientes():
    if not clientes:
        print("No hay clientes registrados.\n")
        return
    for cliente in clientes:
        cliente.mostrar()
    print()

def modificar_cliente():
    id_cliente = input("ID del cliente a modificar: ")
    for cliente in clientes:
        if cliente.id == id_cliente:
            cliente.nombre = input("Nuevo nombre: ")
            cliente.email = input("Nuevo email: ")
            cliente.telefono = input("Nuevo teléfono: ")
            print("Cliente modificado.\n")
            return
    print("Cliente no encontrado.\n")

def eliminar_cliente():
    id_cliente = input("ID del cliente a eliminar: ")
    for cliente in clientes:
        if cliente.id == id_cliente:
            clientes.remove(cliente)
            print("Cliente eliminado.\n")
            return
    print("Cliente no encontrado.\n")

def menu():
    while True:
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_cliente()
        elif opcion == '2':
            mostrar_clientes()
        elif opcion == '3':
            modificar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.\n")

menu()
