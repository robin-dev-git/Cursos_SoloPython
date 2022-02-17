# Expresiones Lambda, Mapas y Filtros

numeros = [1, 2, 3, 4, 5]

def square(num):
    result = num**2
    print(result)
    return result

for item in map(square, numeros):
    print(item)
