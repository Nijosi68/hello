alien_colour = 'red'

# You need to use "is" for strings as opposed to integers

if alien_colour is  'red':
	points = 5
elif alien_colour is 'green':
	points = 10
elif alien_colour is 'blue':
	points = 15
print('Well done. You just earned ' + str(points) + ' points!')

#age = 42

age = input('How old are you? ')
# Note: You need to convert the input string to an integer
age = int(age)

if age < 2:
	stage = 'baby'
elif age < 4:
	stage = 'toddler'
elif age < 13:
	stage = 'child'
elif age < 18:
	stage = 'teenager'
elif age < 60:
	stage = 'adult'
elif age >= 60:
	stage = 'OAP'

if stage is 'adult':
	print('You are an ' + str(stage) + '!')
elif stage is 'OAP':
	print('You are an ' + str(stage) + '!')
else:
	print('You are a ' + str(stage) + '!')
	
