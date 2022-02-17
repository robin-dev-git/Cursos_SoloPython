milista1 = [1, 2, 3, 4, 5, 6, 7, 8]
milista2 = ['a', 'b', 'c']
d = {'k1': 1}
milista3 = [100, 200, 300]

if 'a' in milista2:
    print('Verdadero')
# Verdadero
 
if 'k1' in d:
    print('Verdadero')
# Verdadero

if 'k1' in d.keys():
    print('Verdadero')
else: 
    print('Falso')
# Falso