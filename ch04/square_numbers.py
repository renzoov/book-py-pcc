squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# minimo, maximo y suma
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Minimo: ", min(digits))
print("Maximo: ", max(digits))
print("Suma: ", sum(digits))

# compresión de listas
squares = [value ** 2 for value in range(1, 11)]
print(squares)

