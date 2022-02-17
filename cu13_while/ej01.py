"""
Ciclo WHILE

• Los ciclos WHILE van a continuar ejecutando un bloque de codigo
  while(mientras) una condicion siga siendo verdadera.

• Por ejemplo, while mi carro no tenga gasolina, sigue hechando gas

• O while tenga hambre, comer alimentos.

• Sintaxis para ciclo WHILE
while condicion_boolenana:
    # hacer algo

• Puedes combinar con else
while condicion_booleana:
    # hacer aglo
else:
    # hacer algo distinto

"""

x = 0

while x < 5:
    print(f'El valor actual de x es {x}') # tener cuidado que corriendo infinito de elementos.
    x += 1 # es lo mismo que x = x +1
# El valor actual de x es 0
# El valor actual de x es 1
# El valor actual de x es 2
# El valor actual de x es 3
# El valor actual de x es 4