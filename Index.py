from CRUD import *
from Basic_functions import *
while True:
    print("\n--- ALMACEN DE PELICULAS ---\n")
    print("-- Menu de opciones")
    print("-- 1. Ver todo")
    print("-- 2. Buscar un registro")
    print("-- 3. Agregar nueva pelicula")
    print("-- 4. Actualizar datos de una entrada")
    print("-- 5. Eliminar un registro")
    print("-- 6. Salir del sistema")
    opcion = input("\nIngrese un opcion: ")
    if opcion == "1":
        read_movies()
        input("Presione una tecla para continuar...")
    elif opcion == "2":
        specific_search()
        input("Presione una tecla para continuar...")
    elif opcion == "3":
        movie = create_json_movie()
        create_movie(movie)
        input("Presione una tecla para continuar...")
    elif opcion == "4":
        movie = create_json_update()
        update_movie(movie.get('_id'), movie)
        input("Presione una tecla para continuar...")

    elif opcion == "5":
        delete_movies()

    elif opcion == "6":
        input("Presione una tecla para continuar...")
        exit()
    else:
        print("Opcion no valida!! Ingrese nuevamente....")
