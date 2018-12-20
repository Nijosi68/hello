filename = 'new_file.txt'
with open(filename, 'w') as file_object:
    file_object.write("Hello there. Where did I come from?")
    file_object.write("\nI dont't know, but I've just arrived too!")
    print(filename)
with open(filename) as file_object:
    print(file_object.read())
