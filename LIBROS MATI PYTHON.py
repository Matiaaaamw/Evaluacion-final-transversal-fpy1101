def mostrar_menu():
    print("========== MENU PRINCIPAL ========== ")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")
    print()

def leer_opcion():
    while True:
        opcion = input("Seleccione una opcion: ").strip()
        if opcion.isdigit():
            opcion_int = int(opcion)
            if 1 <= opcion_int <= 6:
                return opcion_int
        print("Opcion inválida. Intente nuevamente.")

libros = []

def validar_titulo(titulo):
    return bool(titulo.strip())

def validar_copias(copias):
    try:
        copias_int = int(copias)
        return copias_int >= 0
    except ValueError:
        return False

def validar_prestamo(prestamo):
    try:
        prestamo_int = int(prestamo)
        return prestamo_int > 0
    except ValueError:
        return False

def agregar_libro(lista):
    titulo = input("Titulo: ").strip()
    if not validar_titulo(titulo):
        print("El titulo del libro no puede estar vacio.")
        return
    
    copias_input = input("Copias: ")
    if not validar_copias(copias_input):
        print("Las copias deben ser un numero entero mayor o igual que 0.")
        return
    copias = int(copias_input)
    
    prestamo_input = input("Prestamo (En dias): ")
    if not validar_prestamo(prestamo_input):
        print("El prestamo debe ser un numero entero mayor que 0.")
        return
    prestamo = int(prestamo_input)
    # Al registrar, la disponibilidad se asigna automaticamente
    disponible = copias > 0
    
    libro = {
        "titulo": titulo,
        "copias": copias,
        "prestamo": prestamo,
        "disponible": disponible
    }
    lista.append(libro)
    print(f"Libro '{titulo}' agregado.")


def buscar_libro(titulo):
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            return libro
    return None


def eliminar_libro(titulo):
    libro = buscar_libro(titulo)
    if libro:
        libros.remove(libro)
        print(f"Libro '{titulo}' eliminado.")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")


def actualizar_disponibilidad(titulo):
    libro = buscar_libro(titulo)
    if libro:
        libro["disponible"] = libro.get("copias", 0) > 0
        print(f"Disponibilidad de '{titulo}' actualizada a {libro['disponible']}.")
    else:
        print(f"Libro '{titulo}' no encontrado.")


def mostrar_libros():
    if not libros:
        print("No hay libros registrados")
        return
    print("\n====== LISTA DE LIBROS ======")
    for libro in libros:
        estado = "DISPONIBLE" if libro['copias'] > 0 else "SIN COPIAS"
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado}")
        print("*" * 29)


def main():
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_libro(libros)
        elif opcion == 2:
            titulo = input("Titulo a buscar: ")
            libro = buscar_libro(titulo)
            if libro:
                print(f"Titulo: {libro['titulo']}, Copias: {libro['copias']}, Prestamo: {libro['prestamo']}, Disponible: {libro['disponible']}")
            else:
                print("Libro no encontrado.")
        elif opcion == 3:
            titulo = input("Titulo a eliminar: ")
            eliminar_libro(titulo)
        elif opcion == 4:
            titulo = input("Titulo para actualizar: ")
            actualizar_disponibilidad(titulo)
        elif opcion == 5:
            mostrar_libros()
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break
        else:
            print("Opcion inválida. Intente nuevamente.")
if __name__ == "__main__":
    main()
