milista1 = [1, 2, 3, 4, 5, 6, 7, 8]
milista2 = ['a', 'b', 'c']
milista3 = [100, 200, 300]

for item in zip(milista1, milista2, milista3):
    print(item)
# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)