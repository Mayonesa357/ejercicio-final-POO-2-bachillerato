class Animales(): #https://susana.informaticailiberis.com/python/8_poo.html enlace ejercicio
    def __init__(self, nombreanimal, tipoespecie, nombrehabitat, peligroextincion):
        self.__nombreanimal = nombreanimal
        self.__tipoespecie = tipoespecie
        self.__nombrehabitat = nombrehabitat
        self.__peligroextincion=peligroextincion

    def set_nombreanimal(self, nombreanimal):
        self.__nombreanimal = nombreanimal

    def get_nombreanimal(self):
        return self.__nombreanimal
    
    def set_tipoespecie(self, tipoespecie):
        self.__tipoespecie = tipoespecie

    def get_tipoespecie(self):
        return self.__tipoespecie
    
    def set_nombrehabitat(self, nombrehabitat):
        self.__nombrehabitat = nombrehabitat

    def get_nombrehabitat(self):
        return self.__nombrehabitat
    
    def set_peligroextincion(self, peligroextincion):
        self.__peligroextincion=peligroextincion

    def get_peligroextincion(self):
        return self.__peligroextincion

class AnAndalucia (Animales): 
    def __init__(self, nombreparque, nombreanimal, tipoespecie, nombrehabitat, peligroextincion):
        self.__nombreparque=nombreparque
        super().__init__(nombreanimal, tipoespecie, nombrehabitat, peligroextincion)
    def set_nombreparque(self, nombreparque):
        self.__nombreparque=nombreparque
    def get_nombreparque(self):
        return self.__nombreparque

zoologico=[] #se inicia la lista donde se almacenara la informacion de los animales


def introduccionDatos(): #introduce los datos del animal y los añade a la lista
    respuesta=input("¿Quiere introducir informacion de un animal? ")
    while respuesta.lower()=="si":
        nombre_animal=input("¿Como se llama su animal? ")
        tipo_especie=input("¿A que especie pertenece? ")
        nombre_habitat=input("¿En que habitat se encuentra? ")
        peligro_extincion=input("¿Se encuentra en peligro de extincion? ")
        animal=Animales(nombre_animal,tipo_especie,nombre_habitat,peligro_extincion)
        if peligro_extincion.lower()=="si": #cambia el atributo segun este en peligro de extincion o no
            animal.set_peligroextincion(True)
        else:
            animal.set_peligroextincion(False)
        zoologico.append(animal)
        respuesta=input("¿Quiere introducir informacion de mas animales? ")

def mostrar(): #muestra los datos de las caracteristicas de los animales añadidos
    for animal in zoologico:
        if animal.get_peligroextincion() == True:
            print("Habitat:",animal.get_nombreanimal(), "Especie:",animal.get_tipoespecie(), "Habitat:",animal.get_nombrehabitat(), "si esta en peligro de extincion")
        else:
            print("Habitat:",animal.get_nombreanimal(), "Especie:",animal.get_tipoespecie(), "Habitat:",animal.get_nombrehabitat(), "no esta en peligro de extincion")



if __name__=='__main__':
    introduccionDatos()
    mostrar()