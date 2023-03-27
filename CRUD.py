from Conection_parameters import collection
import json



def read_movies():
    if collection is not None:
        mayor = 0
        documents = collection.find()
        for document in documents:
            print(document)
            valor = document['_id']
            mayor = valor
        print('Existen %s registros hasta ahora.' % mayor)

    else:
        print("No se encuentran registros aun!!")


def specific_search():
    print("---- Que tipo de busqueda desea efectuar?")
    print("---- 1. Busqueda por fecha de estreno")
    print("---- 2. Busqueda por nombre")
    opcion = int(input("\n---- Ingrese su eleccion: "))

    if opcion == 1:
        year = input("\n---- Ingrese el año que desea consultar: ")
        query = {"year": year}
        document = collection.find_one(query)
        print(document)

    elif opcion == 2:
        name = input("\n---- Ingrese el nombre de la pelicula: ").upper()
        query = {"name": name}
        document = collection.find_one(query)
        print(document)


def create_movie(json_movie):
    result = collection.insert_one(json_movie)
    print(result.inserted_id)


def update_movie(id, json_movie_update):
    query = {"_id": id}
    new_values = {"$set": json_movie_update}
    result = collection.update_one(query, new_values)
    print(result.modified_count)


def delete_movies():
    opcion = input("Conoce el ID de la pelicula? Y = si|N = no").upper()
    if opcion == 'Y':
        id = int(input("Ingrese el id: "))
        result = collection.delete_one({'_id': id})
        print(result.deleted_count)
    elif opcion == "N":
        name = input("Ingrese el nombre de la pelicula: ")
        result = collection.delete_one({'name': name})
        print(result.deleted_count)