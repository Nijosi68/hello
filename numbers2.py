# Start with empty list. Generate list of numbers from 1 to 1m. Print the sum of those numbers. 

numbers = []

for value in range(1,1000001):
	numbers.append(value)

print(sum(numbers))

print(min(numbers))

print(max(numbers))

for value in range(2,100,2):
	print(value)

for value in range(3,33,3):
	print(value)

for value in range(1,11):
	print(value**3)

cubes = [value**3 for value in range(1,11)]
print(cubes)


