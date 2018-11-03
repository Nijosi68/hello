clients = ['rpg', 'sc', 'cls', 'motcomb', 'dalata', 'brindisa', 'tl']
old_clients = []

print(clients)
print(clients[2].upper())
print(clients[0], clients[3])
print(clients[0], clients[1], clients[2])
#Adding a second [?] prints only that number leter in the list string chosen
print(clients[0][2])
print(clients[-2][-2])
clients.append('m&s')
clients.insert(3,'m&g')
print(clients)
sacked_client = 'm&s'
clients.remove(sacked_client)
print(clients)
popped_client = clients.pop(-3)
print(popped_client)
old_clients.append(popped_client)
print(old_clients)
old_clients.append(sacked_client)
print(old_clients)