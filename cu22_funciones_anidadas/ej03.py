
x = 50
 
def func(x):

    # Re Asignacion Local
    x = 200
    print(f'Fui localmente cambiada de x a {x}')

func(x)