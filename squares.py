squares = []

for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

# Clear the list again

squares.clear()

# Now produce the same result with less code, i.e. omitting the "square" variable

for value in range(1,11):
	squares.append(value**2)

print(squares)

