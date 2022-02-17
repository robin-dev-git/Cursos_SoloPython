# herencia y polimorfismo

class Animal():

    def __init__(self):
        print('ANIMAL CREADO')
    
    def quien_soy(self):
        print('Soy un animal')
    
    def comer(self):
        print('Estoy comiendo')

class Perro(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Perro Creado")

    def quien_soy(self):
        print('Soy un perro')


miPerro = Perro()

miPerro.quien_soy()