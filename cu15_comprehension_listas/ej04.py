
celcuis = [0, 10, 20, 34.5]

fahremheit = [((9/5)*temp + 32) for temp in celcuis]
print(fahremheit)
# > [32.0, 50.0, 68.0, 94.1]

print(type(fahremheit))
# > <class 'list'>