"""
• Manera unica de crear una lista de Python rapidamente

• Si te encuentras usando un ciclo for con .append() para crear una
  lista, puedes usar una comprehension en su lugar
"""

mi_cadena = 'hola'

mi_lista = []

for letter in mi_cadena:
    mi_lista.append(letter)

print(mi_lista)
# > ['h', 'o', 'l', 'a']