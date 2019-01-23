responses = {}

polling_active = True

while polling_active:
    name = input("Please enter your name: ")
    response = input("Where would you like to go on hoiliday? ")

    responses[name] = response

    repeat = input("Would you like someone else to take this survey? (y / n): ")
    if repeat == 'n':
        polling_active = False

print('\n------- Poll Results -------')
for name, response in responses.items():
    print(name.title() + " would like to visit " + response.title() + ".")