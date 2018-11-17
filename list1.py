clients =['rpg', 'sc', 'tl', 'cls', 'dhg']
old_clients =[]
print(clients[2].upper())
print(clients[-1])
print(clients[-4])
clients[4] = 'mod'
print(clients)
clients.append('motcomb')
print(clients)
clients.insert(3, 'dukeminster')
print(clients)
del clients[-2]
print(clients)
popped_client = clients.pop(4)
print(popped_client)
print(clients)
old_clients.append(popped_client)
print(old_clients)

# These are examples of slices:

print(clients[0:3])
print(clients[:-1])
print(clients[2:])
print(clients[1:3])

# This is a slice in a loop:

for client in clients[:3]:
	print(client.upper())
