
# mi_diccionario = {'llave1': 'valor1', 'llave2': 'valor2'}

# print(mi_diccionario)
# {'llave1': 'valor1', 'llave2': 'valor2'}

# print(mi_diccionario['llave1'])
# valor1

# --------------------------------------------------

# mi_diccionario = {'manzanas': '2.90', 'agua': '2.90', 'leche': '5.90'}

# print(mi_diccionario['manzanas'])
# 2.90

# mi_diccionario = {'manzanas': '2.90', 'kekes': ['manzana', 'platano'], 'leche': '5.90'}

# print(mi_diccionario)
# {'manzanas': '2.90', 'kekes': ['manzana', 'platano'], 'leche': '5.90'}

# print(mi_diccionario['kekes'][1].upper())
# PLATANO

mi_diccionario = {'manzanas': '2.90', 'kekes': ['manzana', 'platano'], 'leche': '5.90'}

mi_diccionario['gaseosa'] = 5.90

print(mi_diccionario)
# {'manzanas': '2.90', 'kekes': ['manzana', 'platano'], 'leche': '5.90', 'gaseosa': 5.90}

print(mi_diccionario.keys())
# dict_keys(['manzanas', 'kekes', 'leche', 'gaseosa'])

print(mi_diccionario.values())
# dict_values(['2.90', ['manzana', 'platano'], '5.90', 5.9])

print(mi_diccionario.items())
# dict_items([('manzanas', '2.90'), ('kekes', ['manzana', 'platano']), ('leche', '5.90'), ('gaseosa', 5.9)])