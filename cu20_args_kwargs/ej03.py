
def func(**kwargs):
    if 'fruit' in kwargs:
        print('Mi fruta escogida es {}'.format(kwargs['fruit']))
    else:
        print('No hay fruta')

func(fruit='manzana', veggie='lechuga')
# Mi fruta escogida es manzana