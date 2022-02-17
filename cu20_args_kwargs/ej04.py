
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(' Me gustaria {} {}'. format(args[0], kwargs['comida']))

func(10, 30, 50, comida='leche', animal='perro')
# (10, 30, 50)
# {'comida': 'leche', 'animal': 'perro'}
#  Me gustaria 10 leche