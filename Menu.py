
menu = ["Mantenedor de Libros",
        "Reportes",
        "Salir",
        ]

menuMantenedor = ["Agregar libro",
                  "Editar libro",
                  "Eliminar libro",
                  "Buscar libro",
                  "Volver",]

def MenuLibreria():
    print (menu)
    contador = 0
    for i in menu:
        contador += 1
        print(f"[{contador}]-{i}")

    while True:
        opcion = int(input("Opción >> "))
        if opcion == 1:
            print(menuMantenedor)
            contador = 0
            for i in menuMantenedor:
                contador += 1
                print(f"[{contador}]-{i}")
                opcion = int(input("Opción >> "))
                if opcion == 1:
                    print("Ingresa datos para nuevo libro")
                    nuevoLibro = { "LibroID": "",
                    "Titulo": "",
                    "AutorID": "",
                    "CategoriaID": "",
                    "AnoPublicacion": "",
                    "ISBN": ""}
                    for i in nuevoLibro:
                        input("Ingresa ID del libro -> ")
                        input("Ingresa titulo -> ")
                        input("Ingresa ID de categoria -> ")
                        input("Ingresa año de publicacion -> ")
                        input("Ingresa ISBN -> ")
                        return                
        if opcion == len(menuMantenedor):
            break




MenuLibreria()











