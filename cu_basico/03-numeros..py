
print('Esta es una cadena de {}'.format('TEXTO'))
# >>> Esta es una cadena de TEXTO

print('Esta {} {} {}'.format('es', 'una', 'cadena'))
# >>> Esta es una cadena 

print('Esta {0} {0} {0}'.format('es', 'una', 'cadena'))
# >>> Esta es es es 

print('Esta {0} {1} {2}'.format('es', 'una', 'cadena'))
# >>> Esta es una cadena 

print('Esta {e} {u} {c}'.format(e='es', u='una', c='cadena'))
# >>> Esta es una cadena 

print('Esta {e} {e} {e}'.format(e='es', u='una', c='cadena'))
# >>> Esta es es es

# ----------------------------------------

resultado = 100/888

print("Los resultado son {}".format(resultado))



print("Los resultado son {r}".format(r=resultado))

# Formato de float "{valor: width, presicion f}"
print("Los resultado son {r:1.5f}".format(r=resultado))

# ----------------------------------------

nombre = "Eric"
edad = 22

print(f"Los resultado son {nombre} con edad de {edad}")
