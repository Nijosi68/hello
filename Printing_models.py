#Sart with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron', 'sponge bob toy']
completed_models = []

#Simulate printing each design until noe are left
#Move designs to completed models once printed
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
