cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# orden ascendente
cars.sort()
print(cars)

# orden descendente
cars.sort(reverse=True)
print(cars)

print("-------------------------------------")
cars = ['bmw', 'audi', 'toyota', 'subaru']

# ordenar de forma ascendente sin modificar el array original
print("Lista original")
print(cars)

print("Lista ascendente")
print(sorted(cars))

print("Lista original nuevamente")
print(cars)

# ordenar de forma descendente sin modificar el array original
print("Lista original")
print(cars)

print("Lista descendente")
print(sorted(cars, reverse=True))

print("Lista original nuevamente")
print(cars)

print("-------------------------------------")

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Lista original")
print(cars)

# invertir lista con reverse. No modificar de forma alfabetica solo invierte los elementos de la lista
print("Lista invertida")
cars.reverse()
print(cars)

print("Lista original modificada")
print(cars)

print("-------------------------------------")

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Longitud de la lista")
print(len(cars))