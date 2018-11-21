alien_0 = {'colour': 'green', 'points': 5, 'x-position': 0, 'y-position': 25, 'speed': 'fast'}

print("Original x-postion: " + str(alien_0['x-position']))

if alien_0['speed'] == 'slow':
    x_incriment = 1
elif alien_0['speed'] == 'medium':
    x_incriment = 3
elif alien_0['speed'] == 'fast':
    x_incriment = 5

alien_position = alien_0['x-position'] + x_incriment
print("New x-position: " + str(alien_position))
