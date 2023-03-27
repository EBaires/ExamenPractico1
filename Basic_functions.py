import Conection_parameters
from Conection_parameters import *


def create_json_movie():
    mayor = 0
    documents = collection.find()
    for document in documents:
        valor = document['_id']
        mayor = valor
    print("Exiten %s registros hasta ahora."%(mayor))
    movie_name = input("Nombre pelicula: ").upper()
    year = input("Año de estreno: ")
    duration = input("Duracion:  ").upper()
    gender = input("Genero: ").upper()
    director = input("Director: ").upper()
    producer = input("Productora: ").upper()

    movie = {
        "_id": mayor + 1,
        "name": movie_name,
        "year": year,
        "duration": duration,
        "gender": gender,
        "director": director,
        "producer": producer
    }
    documents = collection.find()
    for document in documents:
        print(document)
        valor = document['_id']
        mayor = valor
    return movie


def create_json_update():
    opcion = input("Conoce el ID de la pelicula? Y = si|N = no").upper()
    if opcion == 'Y':
        id = int(input("Ingres el ID a modificar: "))
        print("Menu de opciones")
        print("1. Modificar todos los datos de la pelicula")
        print("2. Modificar un dato de la peilucula")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            movie_name = input("Nombre pelicula: ").upper()
            year = input("Año de estreno: ").upper()
            duration = input("Duracion:  ").upper()
            gender = input("Genero: ").upper()
            director = input("Director: ").upper()
            producer = input("Productora: ").upper()
            movie = {
                "_id": id,
                "name": movie_name,
                "year": year,
                "duration": duration,
                "gender": gender,
                "director": director,
                "producer": producer
            }
            return movie
        elif opcion == "2":
            indice =    input("--- Ingrese el indice: ")
            valor =     input("--- Ingrese el nuevo valor: ")
            movie = {indice: valor}
            return movie
        else:
            print("-------  Dato ingresado no valido!!")
    elif opcion == 'N':
        name = input("Se buscará la pelicula por nombre.\n Ingrese el nombre de la pelicula:").upper()
        print("---- Menu de opciones ----")
        print("---- 1. Modificar todos los datos de la pelicula")
        print("---- 2. Modificar un dato de la peilucula")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            year = input("Año de estreno: ").upper()
            duration = input("Duracion:  ").upper()
            gender = input("Genero: ").upper()
            director = input("Director: ").upper()
            producer = input("Productora: ").upper()
            documents = collection.find()
            for document in documents:
                if document['name'] == name:
                    id = document.get('_id')
            movie = {
                "_id": id,
                "name": name,
                "year": year,
                "duration": duration,
                "gender": gender,
                "director": director,
                "producer": producer
            }
            return movie
        elif opcion == "2":
            indice = input("Ingrese el indice: ")
            valor = input("Ingrese el nuevo valor: ")
            movie = {indice: valor}
            return movie
        else:
            print("Dato ingresado no valido")