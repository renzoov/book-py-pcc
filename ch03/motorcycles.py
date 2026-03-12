motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# agregar elementos a una lista
motorcycles.append('bmw')
print(motorcycles)
motorcycles.append('kawasaki')
print(motorcycles)

# insertar elementos en una lista
motorcycles.insert(0, 'harley-davidson')
print(motorcycles)

# eliminar elementos de una lista usando del
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# eliminar elementos de una lista usando pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
first_motorcycle = motorcycles.pop(1)
print(F"The first motorcycle I owned was a {first_motorcycle.title()}.")

# remover un elemento por valor
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)