first_name = ' peter '
second_name = 'piper'
full_name = first_name.strip().capitalize() + ' ' + second_name.capitalize()
print(full_name.upper())

age = 36
message = 'Hello ' + full_name.title() + '. ' + 'Happy ' + str(age) + 'th Birthday!'
print(message)
print(message.upper())