# Expresiones Lambda, Mapas y Filtros

numeros = [1, 2, 3, 4, 5]

def check_even(num):
    return num % 2 == 0

for n in filter(check_even, numeros):
    print(n)