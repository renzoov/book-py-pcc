motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

print("\n------------------------------\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('kawazaki')
print(motorcycles)

print("\n------------------------------\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(0, 'pulsar')
print(motorcycles)
motorcycles.insert(3, 'ktm')
print(motorcycles)

print("\n------------------------------\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[2]
print(motorcycles)

print("\n------------------------------\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
first_owned = motorcycles.pop(0)
print(popped_motorcycle)
print(first_owned)
print(motorcycles)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(f"The last motorcycle I owned was a {popped_motorcycle.title()}.")

print("\n------------------------------\n")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('honda')
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

print("\n------------------------------\n")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
print(motorcycles[-1])

print("\n------------------------------\n")

motorcycles = []
print(motorcycles[-1])