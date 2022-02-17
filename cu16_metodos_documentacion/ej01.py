"""
# Metodos.

• Objetos creados en Python con una variedad de metodos que podemos usar.

Exploremos con más detalle como podemos encontrar estos metodos.
"""

from random import randint

celcuis = [0, 10, 20, 34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celcuis]

fahrenheit = [float(randint(0, 100))] 

for temp in celcuis:
    fahrenheit.append((9/5)*temp + 32)
print(fahrenheit)