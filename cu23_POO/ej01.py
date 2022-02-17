# Programacion Orientada a Objetos

"""
• Permite a los programadores crear sus propios objetos que tienen
  metodos y atributos

• Podemos llamar distintos metodos que se encuantran en una clase.

• Los metodos actuan como funciones que usan informacion sobre el 
  objetos para poder retornar resultados.

• Podemos crear nuestros propios objetos

• Podemos crear codigo repetible y organizado

• Para los libretos grandes de Pytho necesitamos algo mas que solo
  funciones para organizar todo

• Tareas repetidas son definidas en clases para evitar la redundancia de
 codigo

• veamos un ejemplo


"""
class NombreDeClase():
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def otraFuncion(self):
        # accion
        print(self.param1)

