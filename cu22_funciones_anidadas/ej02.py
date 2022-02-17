# GLobal

name = 'VARIABLE GLOBAL'

def saludo():
    
    #Enclosing
    name = 'Robinson Espejo'

    def hola():

        #local
        name = 'Variable local'
        print('hola ' + name)
    
    hola()

saludo()