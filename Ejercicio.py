class Animales():
    def __init__(self, nombreanimal, tipoespecie, nombrehabitat):
        self.__nombreanimal = nombreanimal
        self.__tipoespecie = tipoespecie
        self.__nombrehabitat = nombrehabitat

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


zoologico=[]


def introduccionDatos():
    global animalesLista
    animalesLista = 0
    respuesta=input("¿Quiere introducir informacion de un animal? ")
    while respuesta.lower()=="si":
        nombre_animal=input("¿Como se llama su animal? ")
        tipo_especie=input("¿A que especie pertenece? ")
        nombre_habitat=input("¿En que habitat se encuentra? ")
        animal=Animales(nombre_animal,tipo_especie,nombre_habitat)
        zoologico.append(animal)
        animalesLista=animalesLista+1
        respuesta=input("¿Quiere introducir informacion de mas animales? ")

def mostrar():
    for animal in zoologico:
        print(animal.get_nombreanimal()) 
        print(animal.get_tipoespecie())
        print(animal.get_nombrehabitat())

def extincion():
    preguntaExtincion = input ("¿Quiere saber si los animales estan en peligro de extincion?")
    while preguntaExtincion.lower()=="si":
        for animal in animalesLista:
            extintos = input ("¿", animal, "se encuentra en peligro de extincion? ")
            if extintos.lower== "si":
                print (animal,"esta en peligro de extincion")
        
if __name__=='__main__':
    introduccionDatos()
    mostrar()
    extincion()