# Inicializamos una lista vacía para las alertas
alertas = []

# Función para crear una nueva alerta
def crear_alerta():
    id_alerta = len(alertas) + 1
    nombre = input("Introduce el nombre de la alerta: ")
    mensaje = input("Introduce el mensaje de la alerta: ")
    nueva_alerta = {
        'id': id_alerta,
        'nombre': nombre,
        'mensaje': mensaje
    }
    alertas.append(nueva_alerta)
    print(f"Alerta creada: {nueva_alerta}\n")

# Función para listar las alertas existentes
def listar_alertas():
    if not alertas:
        print("No hay alertas disponibles.\n")
        return
    for alerta in alertas:
        print(f"ID: {alerta['id']}, Nombre: {alerta['nombre']}, Mensaje: {alerta['mensaje']}")
    print()

# Función para modificar una alerta existente
def modificar_alerta():
    listar_alertas()
    id_alerta = int(input("Introduce el ID de la alerta que deseas modificar: "))
    alerta = next((a for a in alertas if a['id'] == id_alerta), None)

    if alerta:
        nuevo_nombre = input("Introduce el nuevo nombre (deja en blanco si no quieres cambiarlo): ")
        nuevo_mensaje = input("Introduce el nuevo mensaje (deja en blanco si no quieres cambiarlo): ")
        
        if nuevo_nombre:
            alerta['nombre'] = nuevo_nombre
        if nuevo_mensaje:
            alerta['mensaje'] = nuevo_mensaje
        print(f"Alerta modificada: {alerta}\n")
    else:
        print(f"No se encontró ninguna alerta con ID {id_alerta}\n")

# Función para eliminar una alerta
def eliminar_alerta():
    listar_alertas()
    id_alerta = int(input("Introduce el ID de la alerta que deseas eliminar: "))
    alerta = next((a for a in alertas if a['id'] == id_alerta), None)

    if alerta:
        alertas.remove(alerta)
        print(f"Alerta con ID {id_alerta} eliminada.\n")
    else:
        print(f"No se encontró ninguna alerta con ID {id_alerta}\n")

# Menú principal
def menu():
    while True:
        print("1. Crear alerta")
        print("2. Modificar alerta")
        print("3. Eliminar alerta")
        print("4. Listar alertas")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            crear_alerta()
        elif opcion == '2':
            modificar_alerta()
        elif opcion == '3':
            eliminar_alerta()
        elif opcion == '4':
            listar_alertas()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.\n")

# Ejecutamos el programa
menu()