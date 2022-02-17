
x = 50
 
def func():
    global x
    print(f' x es {x}')

    # Re Asignacion Local
    x = 'Nuevo valor'
    print(f'Fui localmente cambiada de x a {x}')

func()
#  x es 50
# Fui localmente cambiada de x a Nuevo valor

print(x)
# Nuevo valor
