def greet_users(names):
    """Print a simple greeting to each use in the list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'bob', 'peter', 'veronica']
greet_users(usernames)