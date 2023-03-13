class Animales():
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
    
    def set_peligroextincion(self,):
        self.__peligroextincion(False) 

    def get_peligroextincion(self):
        return self.__peligroextincion


zoologico=[] #se inicia la lista donde se almacenara la informacion de los animales


def introduccionDatos(): #introduce los datos del animal y los añade a la lista
    global animalesLista 
    animalesLista = 0 #se inicia la variable para usarla como contador
    respuesta=input("¿Quiere introducir informacion de un animal? ")
    while respuesta.lower()=="si":
        nombre_animal=input("¿Como se llama su animal? ")
        tipo_especie=input("¿A que especie pertenece? ")
        nombre_habitat=input("¿En que habitat se encuentra? ")
        animal=Animales(nombre_animal,tipo_especie,nombre_habitat,peligroextincion)
        zoologico.append(animal)
        animalesLista=animalesLista+1
        respuesta=input("¿Quiere introducir informacion de mas animales? ")

def mostrar(): #muestra los datos de las caracteristicas de los animales añadidos
    for animal in zoologico:
        print(animal.get_nombreanimal()) 
        print(animal.get_tipoespecie())
        print(animal.get_nombrehabitat())

def extincion(): #pregunta si el animal esta extinto y si es asi lo confirma
    preguntaExtincion = input ("¿Quiere saber si los animales estan en peligro de extincion? ")
    while preguntaExtincion.lower()=="si":
        for animal in zoologico:
            extintos = input ("¿", animal.get._nombreanimal(), "se encuentra en peligro de extincion? ")
            if extintos.lower()=="si":
                animal.set__peligroextincion(True)
                print (animal,"esta en peligro de extincion")
        
if __name__=='__main__':
    introduccionDatos()
    extincion()
    mostrar()