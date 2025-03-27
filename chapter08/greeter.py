def greet_user():
    """Display a simple greeting"""
    print("Hello!")

greet_user()

# passing information into a function
def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello {username}!")

greet_user("Jada")

# passing a list
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)