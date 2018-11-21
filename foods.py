my_foods = ['pie', 'chips', 'ham', 'eggs']
your_foods = my_foods[:]

print(your_foods)

my_foods.append('sausage')
your_foods.append('yoghurt')

print(my_foods)
print(your_foods)

for food in my_foods:
	print('My favourite food is ' + food + '!')
